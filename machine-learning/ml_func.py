import matplotlib.pyplot as plt
from pathlib import Path
import requests
import sys
from sklearn.metrics import mean_squared_log_error, accuracy_score, mean_squared_error
import pandas as pd


def save_prediction(test_df, yourname):
    test_df[['obs_id', 'event_id', 'reco_energy', 'reco_type']].to_hdf(f'pred_{yourname}.h5',
                                                                       key='pred',
                                                                       complevel=3)

# a function to download a file from a url
def download_file(url, filename, force=False):
    if Path(filename).exists() and not force:
        print(f"File {filename} exists already")
        return None
    with open(filename, "wb") as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')   # total length of the file
        if total_length is None: # no content length header - just download the file
            f.write(response.content)
        else:
            dl = 0  # downloaded size
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=1024):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
                sys.stdout.flush()

def set_plot_style():
    plt.rcParams["figure.figsize"] = (9.23, 9.23 / 3 * 2)
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.max_open_warning"] = 50
    plt.rcParams["font.size"] = 14
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False



    
def scoring(test_file):
    test_labels = pd.read_hdf('escape_school_cta_data_test.h5')
    prediction = pd.read_hdf(test_file)
    df = pd.merge(test_labels, prediction, on=['obs_id', 'event_id'])
    gammas = df[df['true_shower_primary_id']==0]
    mse = mean_squared_log_error(gammas['true_energy'], gammas['reco_energy'])
    acc = accuracy_score(df['true_shower_primary_id'], df['reco_type'])
    return mse, acc

def ranking(directory):
    scores = pd.DataFrame(columns=['name', 'mse', 'acc'])
    for file in Path(directory).glob('*.h5'):
        participant_name = file.stem.replace('pred_', '')
        sc = scoring(file)
        scores = scores.append({'name': participant_name, 'mse': sc[0], 'acc': sc[1]},
                      ignore_index=True
                     )
    scores = scores.sort_values(['mse', 'acc'])
    return scores
    