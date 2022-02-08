
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import matplotlib.dates as mdates
import datetime
import matplotlib.units as munits
converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter

dat = [28.2, 100,
27.6,  95,
27.4,  90,
27.3,  85,
27,    80,
26.35, 70,
25.7,  60,
25,    50,
24.4,  40,
23.9,  30,
23.2,  20,
22.8,  15,
22,    10]
print(dat)
V = np.array(dat[0::2])
perc = np.array(dat[1::2])
print(V)
print(dat)

def getpe3(gli):
    pe = np.interp(gli.Voltage.values, V[ind], perc[ind],)
    ax = axs[1]
    pe2 = np.interp(gli.Voltage.values-1, V[ind], perc[ind],)

    pe3 = np.interp(gli.Voltage.values-1.5, V[ind], perc[ind],)
    gli['pe3'] = ('time', pe3)
    a = gli.pe3.rolling(time=20, center=True).max()
    gli['pe3'] = a
    return gli


with xr.open_dataset('rawnc_realtime/dfo-bb046-rawgli.nc') as gli:
    gli=gli.isel(time=slice(100,None))
    fig, axs = plt.subplots(2, 1, sharex=True, constrained_layout=True)
    ax = axs[0]
    surfOff = 1.5

    ax.plot(gli.time, gli.Voltage, '.', markersize=1)
    a = gli.Voltage.rolling(time=20, center=True).max()
    ax.plot(gli.time, a, label='Surface Voltage')


    ax.plot(gli.time, a - surfOff, label='Surf - 1.5 V')


    ax.axhline(23.9)

    # ax.axhline(23.9+ surfOff)
    ax.set_ylabel('Battery [V]')
    ax.legend()

    ax = axs[1]
    ind = np.argsort(V)
    print(ind)
    pe = np.interp(gli.Voltage.values, V[ind], perc[ind],)
    ax.plot(gli.time, pe,  alpha=0.5)

    gli = getpe3(gli)

    g36 = gli.sel(time=(gli.time > gli.time[-1] - np.timedelta64(36, 'h')))
    g36 = g36.where(np.isfinite(g36.pe3), drop=True)

    t = (g36.time-g36.time[0]).astype(float) / 1e9 /3600 / 24

    p3 = np.polyfit(t, g36.pe3, 1)
    val = np.polyval(p3, t)


    for td in ['../dfo-bb046-20200810/realtime/rawnc_realtime/dfo-bb046046-rawgli.nc', '../dfo-bb046-20200908/realtime/rawnc_realtime/dfo-bb046046-rawgli.nc', '/Users/juliaputko/processing/dfo-bb046/dfo-bb046-20201006/realtime/rawnc_realtime/dfo-bb046-rawgli.nc']:
        #for td in ['../dfo-bb046-20200810/realtime/rawnc_realtime/dfo-bb046046-rawgli.nc', '../dfo-bb046-20200908/realtime/rawnc_realtime/dfo-bb046046-rawgli.nc', '/Users/jklymak/gliderdata/deployments/dfo-bb046/dfo-bb046-20201006/realtime/rawnc_realtime/dfo-bb046-rawgli.nc']:
        with xr.open_dataset(td) as oldgli:
            oldgli = oldgli.where(oldgli.time > np.datetime64('2020-01-01'), drop=True)
            oldgli = getpe3(oldgli)
            ax.plot(oldgli.time-oldgli.time[0] + gli.time[0],
                    oldgli.pe3, color='C7', label='20200717')

    xx = gli.pe3.values[-1]
    ax.plot(gli.time, gli.pe3,  alpha=1,
            label=f'Surf-1.5 V percentage: {xx:1.1f} ', color='C2')
    ax.plot(g36.time, val, label=f'{p3[0]:1.1f} %/day; (last 36 h)', linestyle='--', color='C3')



    ax.legend()

    ax.set_ylim(0, 105)

    ax.axhline(15)
    ax.set_ylabel('Battery %')
    fig.savefig('figs/Battery.png', dpi=300)
