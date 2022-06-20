# flake8: noqa
from astropy.wcs import WCS
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy.visualization import quantity_support

# open image
image_hdu = fits.open('data/casa_1.5-3.0keV.fits.gz')['PRIMARY']
wcs = WCS(image_hdu.header)
image_data = image_hdu.data

# define position and integration radius
pos_casa = SkyCoord('23h23m27.94s', '+58d48m42.4s', frame='icrs')

# create an array of sky positions for each pixel
yp, xp = np.indices(image_data.shape)
sky_positions = SkyCoord.from_pixel(xp=xp, yp=yp, wcs=wcs)

# calculate separation image
separation = pos_casa.separation(sky_positions)

# initialize radius arrays
radii = np.linspace(0, 5, 50).reshape(-1, 1, 1) * u.arcmin
radii_min, radii_max = radii[:-1], radii[1:]

# mask out the annulus regions
mask = (separation > radii_min) & (separation < radii_max)

data_masked = mask * image_data.reshape(-1, 1024, 1024)
data_summed = data_masked.sum(axis=-1).sum(axis=-1)

radius_center = (radii_min[:, 0, 0] + radii_max[:, 0, 0]) / 2.

r_dr = radius_center * (radii_max - radii_min).squeeze()

with quantity_support():
    plt.plot(radius_center, data_summed / (2 * np.pi * r_dr))
    plt.xlabel('Radius (arcmin)')
    plt.ylabel('Profile Amplitude (A.U.)')