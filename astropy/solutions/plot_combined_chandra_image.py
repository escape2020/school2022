# flake8: noqa

# We define a figure size, that has an aspect ratio to accomodate three plots side by side
fig = plt.figure(figsize=(12, 3))
filenames = ['data/casa_0.5-1.5keV.fits.gz', 'data/casa_1.5-3.0keV.fits.gz',
             'data/casa_4.0-6.0keV.fits.gz']

# For convenience we use a Python loop here, but the same can be achieved
# by copy and pasting the code for one energy band
for idx, filename in enumerate(filenames):
    image_hdu = fits.open(filename)['PRIMARY']
    wcs = WCS(image_hdu.header)
    ax = plt.subplot(1, 3, idx + 1, projection=wcs)
    ax.imshow(image_hdu.data, origin='lower', cmap='afmhot')

    # We extract the energy range from the filename, by setting it "by hand" is also fine
    energy_range = filename[10:20]
    ax.set_title('Energy range: {}'.format(energy_range))

    ax.set_xlabel('RA (deg)')
    ax.set_ylabel('DEC (deg)')