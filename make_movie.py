#!/usr/bin/env python

import sys
import argparse
import matplotlib.pyplot as plt
from matplotlib import animation

import numpy as np
import netCDF4 as nc

"""
This script makes a fluid animation using NetCDF data.

Type ./fluid_movie.py --help to get usage.
"""

def main():
    # Set up some arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="Input file containing our data")
    parser.add_argument('field_name', help="Name of data field to animate")
    args = parser.parse_args()
    
    # Open a netcdf file. The name of the file is in arg._input_file
    # This is the same as saying:
    """
    with nc.Dataset(args.input_file) as f:
        vorticity = f.variables['vorticity_z']
    """
    f = nc.Dataset(args.input_file)
    vorticity = f.variables['vorticity_z']
    # Vorticity is a multi-dimensional dataset, the dimensions are:
    # Time [days], depth [dbars], yt_ocean [degrees N], xt_ocean[degrees E]
    vorticity = vorticity[:]
    """
    # This code will be removed.
    import pdb
    pdb.set_trace()
    """
    
    # Select the firt time point, the surface then all latitude and longitude points.
    #plt.imshow(vorticity[0,0,:,:])
    # To show the plot immediately instead of saving to a file replace the line below with this one:
    # plt.show()
    
    # To save the plot as an image:
    #plt.savefig('vorticity.png')
    number_of_times = vorticity.shape[0]
    # for t in range(0, len(f.variables['Time']))
    
    #fig = plt.figure()
    #images = []
    
    for t in range(0,number_of_times):
        img = plt.imshow(vorticity[t,0,:,:])
        images.append([img])
        # Can use 'string' + str(int) OR 'string%d % int OR 'string{}'.format(int)
        output_file_name = 'vorticity_%03d.png' % t
        # output_file_name = 'vorticity_' + str(t).zfill(3) + '.png'
        # output_file_name = 'vorticity_{}'.format(t,'03') + '.png'
        plt.savefig(output_file_name)
        plt.close()
        #print t

    #ani = animation.ArtistAnimation(fig, images, interval = 20)
    #plt.show()
    # Extra:
    # Want the vorticity to have format vorticity_<t>.png
    # Ideally this would be padded with 0's. For example,
    # vorticity_001.png
    # See:
    # http://stackoverflow.com/questions/339007/nicest-way-to-pad-zeroes-to-string
    
    # More extra:
    # Once you have a collection of images, see if you can find a program to join them all together into
    # a movie. There ma be a way to do this in Python which be good because then we can make a self
    # contained program. Alternatively, if there is an external program which we can call from within
    # our Python program that would be good too.
    # ffmpeg
    # avconv -r 25 -i vorticity_%3d.png
    # Close the netcdf file.
    f.close()

    
    print "I'm in the main function."
    return True

if __name__ == "__main__":
    sys.exit(main())