import logging
import os
import pyglider.ncprocess as ncprocess
import pyglider.plotting as pgplot
import pyglider.slocum as slocum

logging.basicConfig(level='DEBUG')

binarydir  = './realtime_raw/'
rawdir     = './realtime_rawnc/'
cacdir     = './cac/'
sensorlist = './dfo-walle652_sensors.txt'
deploymentyaml = './deploymentRealtime.yml'
l1tsdir    = './L0-timeseries/'
profiledir = './L0-profiles/'
griddir    = './L0-gridfiles/'
plottingyaml = './plottingconfig.yml'
scisuffix    = 'tbd'
glidersuffix = 'sbd'

os.system('rsync -av --no-perms --chmod=a+rX cproof@sfmc.webbresearch.com:/var/opt/sfmc-dockserver/stations/dfo/gliders/ ~/processing/slocum_dockserver/')
# os.system('source synctodfo.sh')
#os.system('rsync -av ~/gliderdata/slocum_dockserver/wall_e_652/from-glider/*2019-3* ' + binarydir)
os.system('rsync -av ~/processing/slocum_dockserver/wall_e_652/from-glider/*2021-* ' + binarydir)

print(scisuffix)
if 1:
    # turn *.EBD and *.DBD into *.ebd.nc and *.dbd.nc netcdf files.
    slocum.binary_to_rawnc(binarydir, rawdir, cacdir, sensorlist, deploymentyaml,
            incremental=True, scisuffix=scisuffix, glidersuffix=glidersuffix)

    # remove some bad files:
    # os.system('rm realtime_rawnc/017*')
    # os.system('rm realtime_rawnc/0180*')
    # merge individual neetcdf files into single netcdf files *.ebd.nc and *.dbd.nc
    slocum.merge_rawnc(rawdir, rawdir, deploymentyaml,
            scisuffix=scisuffix, glidersuffix=glidersuffix)
print('Done merge')

if 1:
    # Make level-1 timeseries netcdf file from th raw files...
    outname = slocum.raw_to_L1timeseries(rawdir, l1tsdir, deploymentyaml,
              profile_filt_time=400, profile_min_time=100)
    # make profile netcdf files for ioos gdac...
    #ncprocess.extract_L1timeseries_profiles(outname, profiledir, deploymentyaml)
    # make grid of dataset....

    pgplot.timeseries_plots(outname, plottingyaml)

    outname2 = ncprocess.make_L2_gridfiles(outname, griddir, deploymentyaml,
                                           dz=10)
    pgplot.grid_plots(outname2, plottingyaml)
