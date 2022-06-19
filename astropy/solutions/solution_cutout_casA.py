from astropy.nddata.utils import Cutout2D
from astropy.wcs import WCS

image_hdu = fits.open('data/casa_0.5-1.5keV.fits.gz')['PRIMARY']
wcs = WCS(image_hdu.header)
image_data = image_hdu.data

pos_casa = SkyCoord('23h23m27.94s', '+58d48m42.4s', frame='icrs')

data_cutout = Cutout2D(image_data, position=pos_casa,
                       wcs=wcs, size=0.05 * u.deg)

# Find index of maximum value (this will return the
# index on the flattened array)
idx_flat = data_cutout.data.argmax()

# Transform back to the original shape
idx = np.unravel_index(idx_flat, data_cutout.data.shape)

# Transform to SkyCoord
pos = SkyCoord.from_pixel(*idx, wcs=data_cutout.wcs)
print("The position of the brightest pixel in the image is: {}".format(pos))