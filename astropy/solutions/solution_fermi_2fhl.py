# Read table
fermi_2fhl = Table.read('data/fermi_2fhl_catalog.fits', hdu=1)

# Sort by brightness
fermi_2fhl.sort('Flux50')

# With -1 we get the last element
print('The brightest source in the catalog is: {} \n'.format(fermi_2fhl[-1]['ASSOC']))

# you can also use argmax
#index_brightest_source=fermi_2fhl['Flux50'].argmax()
#brighest_source = fermi_2fhl['ASSOC'][index_brightest_source]
#print('The brightest source in the catalog is: {} \n'.format(brighest_source[0]))


# Define SkyCoord for all objects in the table
coords = SkyCoord(fermi_2fhl['GLON'], fermi_2fhl['GLAT'], frame='galactic')

# Get Crab position
coord_crab = coords[fermi_2fhl["ASSOC"] == "Crab"]

# Find rows where separation < 1 deg
separation = coord_crab.separation(coords)

# Print result
max_separation = 10 * u.deg
fermi_2fhl[separation < max_separation]