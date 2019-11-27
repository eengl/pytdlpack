#!/usr/bin/env python

import numpy as np
import pdb
import os
import sys

import setuptools
platform = setuptools.distutils.util.get_platform()
build_path = './build/lib.'+platform+'-'+str(sys.version_info.major)+'.'+str(sys.version_info.minor)
sys.path.insert(0,build_path)
import pytdlpack
import TdlpackIO

# ---------------------------------------------------------------------------------------- 
# Point stdout to null
# ---------------------------------------------------------------------------------------- 
fout = open(os.devnull,'w')
sys.stdout = fout

# ---------------------------------------------------------------------------------------- 
# Open vector TDLPACK file; iterate; close
# ---------------------------------------------------------------------------------------- 
f = TdlpackIO.open("sampledata/hre201701")
rec = f.select(date=2017011512)
f.close()

fout.close()