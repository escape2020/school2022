source_classes = set(fermi_2fhl['CLASS'])

print('Source classes: {}'.format(source_classes))

from astropy.coordinates import Angle

plt.figure(figsize=(12, 5))
ax = plt.subplot(projection='aitoff')

glon = Angle(fermi_2fhl['GLON'].quantity)
glon = glon.wrap_at('180d')

glat = Angle(fermi_2fhl['GLAT'].quantity)

with quantity_support():
    for source_class in sorted(source_classes):
        selection = fermi_2fhl['CLASS'] == source_class
        ax.scatter(glon[selection].rad, glat[selection].rad, label=source_class)
    ax.grid()
    plt.legend(bbox_to_anchor=(1.15, 1), loc=1)