import glob
import create_data_dict as cdf
from scipy import linspace, io
from pylab import *

# Import the data
f_list = glob.glob('data/H*/Tagged_*.bin')
f1 = f_list[0]
taggingInfo, df1, df2 = cdf.create_data_dict(f1)

# Plot L1_Real and L2_Real

# Gets the timestamp range from the tagging data
def get_tagging_max_min(taggingInfo):
    tags = []
    for i in range(len(taggingInfo)):
        tags.append(taggingInfo[i, 2])
        tags.append(taggingInfo[i, 3])
    return max(tags), min(tags)


# Gets the cooresponding index ranges based on the 
# tagging data
def get_time_tick_index(timetick, mx, mn):
    lag_tick = 0
    for i, tick in enumerate(timetick):
        if tick > mx and lag_tick <= mx:
            idx_stop = i
        elif tick > mn and lag_tick <= mn:
            idx_start = i
        lag_tick = tick
    return idx_start, idx_stop    


# Use the index info to get the appropriate subset of data
mx1, mn1 = get_tagging_max_min(taggingInfo)
idx_start1, idx_stop1 = get_time_tick_index(df1['L1_TimeTicks'], mx1, mn1)
subset1 = np.array(xrange(int(round(idx_start1*0.999, -3)),int(round(idx_stop1*1.001, -3))))

mx2, mn2 = get_tagging_max_min(taggingInfo)
idx_start2, idx_stop2 = get_time_tick_index(df2['L2_TimeTicks'], mx2, mn2)
subset2 = np.array(xrange(int(round(idx_start2*0.999, -3)),int(round(idx_stop2*1.001, -3))))

# Plots the stop and start of individual devices
def plot_devices(p, taggingInfo, df):
    top = max(df)
    bottom = min(df)
    for i in range(len(taggingInfo)):
        p.plot([taggingInfo[i,2], taggingInfo[i,2]], [bottom, top],  c='g')
        p.plot([taggingInfo[i,3], taggingInfo[i,3]], [bottom, top], c='r')


# Plot L1
fig1 = figure(1)
ax1 = fig1.add_subplot(411)
ax1.plot(df1['L1_TimeTicks'][subset1], df1['L1_Real'][subset1])
plot_devices(ax1, taggingInfo, df1['L1_Real'][subset1])

ax2 = fig1.add_subplot(412)
ax2.plot(df1['L1_TimeTicks'][subset1], df1['L1_Imag'][subset1], c='r')
plot_devices(ax2, taggingInfo, df1['L1_Imag'][subset1])

ax3 = fig1.add_subplot(413)
ax3.plot(df1['L1_TimeTicks'][subset1], df1['L1_Pf'][subset1], c='g')
plot_devices(ax3, taggingInfo, df1['L1_Pf'][subset1])

# Plot L2
fig2 = figure(2)
ax4 = fig2.add_subplot(411)
ax4.plot(df2['L2_TimeTicks'][subset2], df2['L2_Real'][subset2])
plot_devices(ax4, taggingInfo, df2['L2_Real'][subset2])

ax5 = fig2.add_subplot(412)
ax5.plot(df2['L2_TimeTicks'][subset2], df2['L2_Imag'][subset2], c='r')
plot_devices(ax5, taggingInfo, df2['L2_Imag'][subset2])

ax6 = fig2.add_subplot(413)
ax6.plot(df2['L2_TimeTicks'][subset2], df2['L2_Pf'][subset2], c='g')
plot_devices(ax6, taggingInfo, df2['L2_Pf'][subset2])

show()
