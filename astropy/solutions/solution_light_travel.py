# flake8: noqa

from astropy import constants as const
import astropy.units as u

# distance sun - earth
distance_sun = 1 * u.au

# speed of light
speed = const.c

# time
time_sun = distance_sun / speed
print("Light travels from sun to earth in {:.2f}".format(time_sun.to('min')))

# distance to GC
distance_gc = 8 * u.kpc

# time
time_gc = distance_gc / speed
print("Light travels from the GC to earth in {:.2f}".format(time_gc.to('yr')))
