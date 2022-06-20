#!/usr/bin/env python

import argparse

from math import pi

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Computes the volume of a sphere given a radius in "
                                                 "meters.")
    parser.add_argument(
        '--radius',
        '-r',
        type=float,
        dest='radius',
        help='Personal access token to (sandbox)Zenodo',
        default=10
    )
    args = parser.parse_args()

    radius = args.radius
    vol = 4 / 3 * pi * radius**3

    print('The volume of a sphere with radius {:.2f} m is {:.2f} m**3'.format(radius, vol))
