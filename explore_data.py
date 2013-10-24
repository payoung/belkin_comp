import glob
import create_data_dict as cdf
from scipy import linspace, io
from pylab import *


f_list = glob.glob('data/H*/Tagged_*.bin')

f1 = f_list[0]

taggingInfo, df1, df2 = cdf.create_data_dict(f1)


def add_devices(ax,taggingInfo,timeticks,bottom=300,step=300):
    """
    Add a green line for every device.
    First device will be at y=bottom, second at y=bottom+step etc
    Device names will be displayed on the left
    """
    for i in range(len(taggingInfo)):
        ax.plot([taggingInfo[i,2],taggingInfo[i,3]], [i*step+bottom,i*step+bottom], color=(0,1,0,0.5), linewidth=10)
        str1 = '%s' % taggingInfo[i,1]
        ax.text(timeticks[0],step*i+bottom, str1)


#Plot L1_Real and L2_Real

print type(taggingInfo)
print taggingInfo
print len(taggingInfo)

fig1 = figure(1)
ax1 = fig1.add_subplot(411)
ax1.plot(df1['L1_TimeTicks'], df1['L1_Real'])

ax2 = fig1.add_subplot(412)
ax2.plot(df1['L1_TimeTicks'], df1['L1_Imag'])

ax3 = fig1.add_subplot(413)
ax3.plot(df1['L1_TimeTicks'], df1['L1_Pf'])

fig2 = figure(2)
ax4 = fig2.add_subplot(411)
ax4.plot(df2['L2_TimeTicks'], df2['L2_Real'])

ax5 = fig2.add_subplot(412)
ax5.plot(df2['L2_TimeTicks'], df2['L2_Imag'])

ax6 = fig2.add_subplot(413)
ax6.plot(df2['L2_TimeTicks'], df2['L2_Pf'])

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

