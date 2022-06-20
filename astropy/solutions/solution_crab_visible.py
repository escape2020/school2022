# flake8: noqa
from astropy.coordinates import EarthLocation, AltAz
from astropy.time import Time
import numpy as np
from astropy.visualization import quantity_support

# Define coordinate
coord_crab = SkyCoord(83.63 * u.deg,  22.01 * u.deg, frame='icrs')

# Set location
annecy = EarthLocation(lat=45.8058 * u.deg, lon=6.5726 * u.deg)

# Define array of times (30 minute intervals)
time_intervals = np.linspace(0 * u.day, 1 *u.day, 48)

time_start = Time('2022-06-22 00:00:00')
times = Time(time_start + time_intervals)

# Get AltAz coordinates
altaz = AltAz(obstime=times, location=annecy)
crab_altaz = coord_crab.transform_to(altaz)

# Get altitude over horizon
altitudes = crab_altaz.alt.to('deg')

# Get times when altitude > 0
above_horizon = altitudes > 0 * u.deg

with quantity_support():
    plt.plot_date(times.plot_date, altitudes, fmt='-')

    # orient date labels at a slant
    plt.gcf().autofmt_xdate()

    alt_min, alt_max = -25 * u.deg, 75 * u.deg
    plt.fill_between(times.plot_date,
                     alt_min, alt_max,
                     where=above_horizon,
                     facecolor='green',
                     alpha=0.5)
    plt.ylim(alt_min, alt_max)
