# flake8: noqa
from astropy.io import fits

filenames = ['data/casa_0.5-1.5keV.fits.gz', 'data/casa_1.5-3.0keV.fits.gz',
             'data/casa_4.0-6.0keV.fits.gz']

data_list = []

for filename in filenames:
    image_hdu = fits.open(filename)['PRIMARY']
    data_list.append(image_hdu.data)

data_summed = np.sum(data_list, axis=0)
plt.imshow(data_summed, origin='lower', cmap='afmhot')