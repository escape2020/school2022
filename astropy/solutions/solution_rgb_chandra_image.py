# flake8: noqa
from astropy.visualization import AsinhStretch

filenames = ['data/casa_0.5-1.5keV.fits.gz', 'data/casa_1.5-3.0keV.fits.gz',
             'data/casa_4.0-6.0keV.fits.gz']

# use asinh stretching to brighten up the image
stretch = AsinhStretch(0.1)

data_rgb = []

for filename in filenames:
    image_hdu = fits.open(filename)['PRIMARY']
    data = image_hdu.data
    data /= data.max()
    data = stretch(data)
    data_rgb.append(data)

data_rgb_stacked = np.stack(data_rgb, axis=2)

plt.figure(figsize=(10, 10))
ax = plt.subplot(projection=wcs)
ax.imshow(data_rgb_stacked, origin='lower')

ax.set_xlabel('RA (deg)')
ax.set_ylabel('DEC (deg)')

"""
#To use the make_lupton_rgb astropy function
from astropy.visualization import make_lupton_rgb

data_rgb=make_lupton_rgb(data_rgb[0],data_rgb[1],data_rgb[2], Q=0.1, stretch=1)
plt.figure(figsize=(10, 10))
ax = plt.subplot(projection=wcs)
ax.imshow(data_rgb, origin='lower')

ax.set_xlabel('RA (deg)')
ax.set_ylabel('DEC (deg)')
"""