# flake8: noqa

# Coordinate of PKS2155-305
# coord_pks = SkyCoord.from_name('pks2155-304')
coord_pks = SkyCoord("21h58m52.7s", "-30d13m18s", frame="icrs")

# Coordinate of the Crab Nebula
# coord_crab = SkyCoord.from_name('crab')
coord_crab = SkyCoord(83.63 * u.deg,  22.01 * u.deg, frame='icrs')

separation_crab = coord_pks.separation(coord_crab)
print('The angular distance between PKS2155-204 and the Crab Nebula is {:.2f}'.format(separation_crab))

# Coordinate of the Galactic Center
coord_gc = SkyCoord(0, 0, unit='deg', frame='galactic')
separation_gc = coord_pks.separation(coord_gc)
print('The angular distance between PKS2155-204 and the Galactic Center is {:.2f}'.format(separation_gc))
