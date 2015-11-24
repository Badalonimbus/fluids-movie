#!/usr/bin/env python

import sys
import argparse

import numpy as np
import netCDF4 as nc

"""
This script makes a fluid animation using NetCDF data.
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help="Input file containing our data")
    parser.add_argument('field_name', help="Name of data field to animate")
    args = parser.parse_args()
    
    print "I'm in the main function."
    return True

if __name__ == "__main__":
    sys.exit(main())