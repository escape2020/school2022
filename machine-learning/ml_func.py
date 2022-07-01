import matplotlib.pyplot as plt
from pathlib import Path
import requests
from tqdm.auto import tqdm



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
            total_length = int(total_length)
            bar = tqdm(total=total_length, unit_scale=True, unit='B')
            for data in response.iter_content(chunk_size=50*1024):
                bar.update(len(data))
                f.write(data)

def set_plot_style():
    plt.rcParams["figure.figsize"] = (9.23, 9.23 / 3 * 2)
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.max_open_warning"] = 50
    plt.rcParams["font.size"] = 14
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False


