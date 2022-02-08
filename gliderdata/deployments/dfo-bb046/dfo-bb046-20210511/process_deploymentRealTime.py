import sys 

sys.path.append('/Users/juliaputko/pyglider')

import logging
import os
import pyglider.seaexplorer as seaexplorer
import pyglider.ncprocess as ncprocess
import pyglider.plotting as pgplot

logging.basicConfig(level='INFO')
sourcedir = '~alseamar/gliderdata/SEA046/000060/C-Csv/*'
rawdir  = './raw/'
rawncdir     = './rawnc_realtime/'
deploymentyaml = './deployment.yml'
l1tsdir    = './L0-timeseries/'
profiledir = './L0-profiles/'
griddir    = './L0-gridfiles/'
plottingyaml = './plottingconfig.yml'

os.system('rsync -av ' + sourcedir + ' ' + rawdir)

# turn *.EBD and *.DBD into *.ebd.nc and *.dbd.nc netcdf files.
if 1:
    seaexplorer.raw_to_rawnc(rawdir, rawncdir, deploymentyaml)
    # remove some early bad files:
    os.system('rm rawnc_realtime/*0001*.nc')
    os.system('rm rawnc_realtime/*0002*.nc')
    os.system('rm rawnc_realtime/*0003*.nc')
    os.system('rm rawnc_realtime/*0004*.nc')
    os.system('rm rawnc_realtime/*0005*.nc')
    
    # merge individual neetcdf files into single netcdf files *.ebd.nc and *.dbd.nc
    seaexplorer.merge_rawnc(rawncdir, rawncdir, deploymentyaml, kind='sub')
    # Make level-1 timeseries netcdf file from th raw files...
outname = seaexplorer.raw_to_L1timeseries_raw(rawncdir, l1tsdir,
    deploymentyaml, kind='sub', profile_filt_time=400,
    profile_min_time=100)
if 1:
    # make profile netcdf files for ioos gdac...
    #ncprocess.extract_L1timeseries_profiles(outname, profiledir, deploymentyaml)
    outname2 = ncprocess.make_L2_gridfiles(outname, griddir, deploymentyaml)

    # make grid of dataset....
    pgplot.timeseries_plots(outname, plottingyaml)


    pgplot.grid_plots(outname2, plottingyaml)
