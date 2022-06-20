# flake8: noqa
import astropy.units as u

# define new unit baro-meter
bm = u.def_unit('baro-meter', 25 * u.cm)
u.add_enabled_units(bm)

# height of the empire state building
height = 381 * u.m

# convert to baro-meters
height_bm = height.to("baro-meter")
print("The height of the empire state building in baro-meters is {}".format(height_bm))
