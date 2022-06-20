# flake8: noqa
# Get example table
from astropy.table import Table

table = Table()
table['Source_Name'] = ['Crab', 'Sag A*', 'Cas A']
table['GLON'] = [184.55754381, 0, 111.74169477] * u.deg
table['GLAT'] = [-5.78427369, 0, -2.13544151] * u.deg

# Create SkyCoord object holding all 3 sky coordinates
coords = SkyCoord(table['GLON'], table['GLAT'], frame='galactic')

# Add new columns
table['RA'] = coords.icrs.ra
table['DEC'] = coords.icrs.dec

table