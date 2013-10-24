import glob
import create_data_dict as cdf
from scipy import linspace, io
from pylab import *

f_list = glob.glob('data/H*/Tagged_*.bin')

f1 = f_list[0]

taggingInfo, df1, df2 = cdf.create_data_dict(f1)


def plot_devices(p, taggingInfo, df):
    top = max(df)
    bottom = min(df)
    for i in range(len(taggingInfo)):
        p.plot([taggingInfo[i,2], taggingInfo[i,2]], [bottom, top],  c='g')
        p.plot([taggingInfo[i,3], taggingInfo[i,3]], [bottom, top], c='r')


#Plot L1_Real and L2_Real

print type(taggingInfo)
print taggingInfo
print len(taggingInfo)
print len(df1['L1_TimeTicks'])
print len(df2['L2_TimeTicks'])


def get_tagging_max_min(taggingInfo):
    tags = []
    for i in range(len(taggingInfo)):
        tags.append(taggingInfo[i, 2])
        tags.append(taggingInfo[i, 3])
    return max(tags), min(tags)


mx1, mn1 = get_tagging_max_min(taggingInfo)


def get_time_tick_index(timetick, mx, mn):
    lag_tick = 0
    for i, tick in enumerate(timetick):
        if tick > mx and lag_tick <= mx:
            idx_stop = i
        elif tick > mn and lag_tick <= mn:
            idx_start = i
        lag_tick = tick
    return idx_start, idx_stop    


idx_start, idx_stop = get_time_tick_index(df1['L1_TimeTicks'], mx1, mn1)

print mn1, mx1
print idx_start, idx_stop
#print df1['L1_TimeTicks'][idx_start], df1['L1_TimeTicks'][idx_stop]

subset = np.array(xrange(213000,216000))
#subset = np.array( xrange(300000,360000))

print df1['L1_TimeTicks'][300000], df1['L1_TimeTicks'][360000]

fig1 = figure(1)
ax1 = fig1.add_subplot(411)
ax1.plot(df1['L1_TimeTicks'][subset], df1['L1_Real'][subset])
plot_devices(ax1, taggingInfo, df1['L1_Real'][subset])

ax2 = fig1.add_subplot(412)
ax2.plot(df1['L1_TimeTicks'][subset], df1['L1_Imag'][subset], c='r')
plot_devices(ax2, taggingInfo, df1['L1_Imag'][subset])

ax3 = fig1.add_subplot(413)
ax3.plot(df1['L1_TimeTicks'][subset], df1['L1_Pf'][subset], c='g')
plot_devices(ax3, taggingInfo, df1['L1_Pf'][subset])


"""
fig2 = figure(2)
ax4 = fig2.add_subplot(411)
ax4.plot(df2['L2_TimeTicks'], df2['L2_Real'])

ax5 = fig2.add_subplot(412)
ax5.plot(df2['L2_TimeTicks'], df2['L2_Imag'], c='r')

ax6 = fig2.add_subplot(413)
ax6.plot(df2['L2_TimeTicks'], df2['L2_Pf'], c='g')
"""
show()

"""
# ======================================================================
# Plotting
# subset is the range of indices of L1_TimeTicks to plot
subset = np.array( xrange(300000,360000))

fig = figure(1)
fig.set_dpi(150)
fig.set_size_inches(18.5,50.5)
# Plot real power consumption
ax1 = fig.add_subplot(411)
#ax1.set_xlim(df1['L1_TimeTicks'][0],df1['L1_TimeTicks'][1])
ax1.plot(df1['L1_TimeTicks'][subset], df1['L1_Real'][subset], color='blue')
ax1.set_title('Real Power (W) and device ON time')
add_devices(ax1,taggingInfo,df1['L1_TimeTicks'][subset])
# This will draw a green line for every device while it is turned on
    
# Plot Imaginary/Reactive power (VAR)
ax2 = fig.add_subplot(412)
ax2.plot(df1['L1_TimeTicks'][subset],df1['L1_Imag'][subset])
ax2.set_title('Imaginary/Reactive power (VAR)')
add_devices(ax2,taggingInfo,df1['L1_TimeTicks'][subset])

# Plot Power Factor
ax3 = fig.add_subplot(413)
ax3.plot(df1['L1_TimeTicks'][subset],df1['L1_Pf'][subset])
ax3.set_title('Power Factor');
ax3.set_xlabel('Unix Timestamp');
add_devices(ax3,taggingInfo,df1['L1_TimeTicks'][subset],bottom=0.25,step=0.1)

show()
"""

