"""Example script to use with a debugger. 

It opens the Fermi point-source catalog, extracts some data (the
RA/Dec and the columns specified by the user), and makes a spatial and
histogram plot of each of the user columns.
"""

from astropy.table import Table
from astropy import coordinates as c
from astropy import units as u
import matplotlib.pyplot as plt
import numpy as np


def get_data(catalog, cols):
    """
    Read some data columns from a FITS catalog.

    Parameters
    ----------
    catalog : str
        filename of catalog
    cols: list(str)
        list of extra column names to extract

    Returns
    -------
    np.ndarray, np.ndarray, list(np.ndarray):
        ra, dec, [col1, ...]
    """
    table = Table.read(catalog)
    return table[cols]


def make_plot(gal_l, gal_b, value, title):
    """Plot the spatial distribution of the value on the left, and a
    histogram on the right.
    """
    fig = plt.figure(figsize=(10, 5), tight_layout=True)

    good = value > 0

    gval = value[good]
    sizes = gval / gval.max() * 100

    plt.subplot(1, 2, 1)
    plt.scatter(gal_l[good], gal_b[good], c=np.log10(value[good]), alpha=0.5, s=sizes)
    plt.xlabel("Galactic Longitude")
    plt.ylabel("Galactic Latitude")
    cb = plt.colorbar()
    cb.set_label(title)

    plt.subplot(1, 2, 2)
    plt.hist(np.log10(value[good]), log=True)
    plt.xlabel(f"log10({title})")
    plt.ylabel("number of sources")


@u.quantity_input(ra=u.deg, deg=u.deg)
def convert_to_gal(ra, dec):
    """Convert an array of RA/Dec values to GalL/GalB in degrees"""
    coord = c.SkyCoord(ra, dec, frame=c.ICRS)
    gcoord = coord.galactic
    lon = gcoord.l.to_value(u.deg)
    lat = gcoord.b.to_value(u.deg)
    lon[lon > 180] -= 360.0  # make 0,0 the center

    return lon, lat


if __name__ == "__main__":

    plt.style.use(["ggplot", "seaborn-poster"])

    radec_cols = ["RAJ2000", "DEJ2000"]
    data_cols = ["Variability_Index", "Spectral_Index"]
    cols = radec_cols + data_cols

    data = get_data("gll_psc_v14.fit.gz", cols=cols)
    gal_l, gal_b = convert_to_gal(data["RAJ2000"], data["DEJ2000"])

    for col in data_cols:
        make_plot(gal_l, gal_b, data[col], title=col)
        plt.show()
