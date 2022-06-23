import pandas as pd
from ctapipe.io import TableLoader
from ctapipe.utils import get_dataset_path


import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
import collections
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap, to_hex
from pathlib import Path
import requests
import sys

from ctapipe.instrument import SubarrayDescription


rng = np.random.default_rng(0)


colors = ['xkcd:sky', 'xkcd:grass']
cmap = ListedColormap(colors)


gamma_filename = get_dataset_path('gamma_diffuse_dl2_train_small.dl2.h5')
proton_filename = get_dataset_path('proton_dl2_train_small.dl2.h5')

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
    sns.reset_orig()
    plt.rcParams["figure.figsize"] = (9.23, 9.23 / 3 * 2)
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.max_open_warning"] = 50
    plt.rcParams["font.size"] = 14
    plt.rcParams["lines.linewidth"] = 2
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False


def read_events(path):

    loader = TableLoader(
        path,
        load_dl2_geometry=True,
        load_instrument=True,
        load_simulated=True,
    )

    table = loader.read_telescope_events()

    # these two columns are arrays in each row, which is not supported by pandas
    table.remove_columns(['tels_with_trigger', 'HillasReconstructor_tel_ids'])

    # convert astropy.table.Table to pd.DataFrame
    table = table.to_pandas()
    forbidden_columns = 'obs_id|event_id'
    table = table.filter(regex=f'^(?!{forbidden_columns}).*$')
    return table


def get_gammas():
    gamma_path = gamma_filename
    return read_events(gamma_path)
    
def get_protons():
    proton_path = proton_filename
    return read_events(proton_path)

