import sys
import numpy as np
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#THIS PROGRAM PLOTS DATA IN FORM 'x, y'


plot_title=" "

x_axis=" "
y_axis=" "

#fig=plt.figure(figsize=(10,5))

#f2 = open('time_stats_run1temp.txt' , "r")

filename = 'time_stats_run1temp.txt'
#with open('time_stats_run1temp.txt' , "r") as f2:
thread_list = [1, 4, 8, 16, 32]
N_size_list = [2000, 4000, 8000]

#for line in f2:
npdata = np.loadtxt(filename)
"""
print npdata 
print
print npdata[0]
print 
print npdata[0][0]
"""


xdata = []
ydata = []
print("Data should be structured (Real, User, Sys)...")

for idx, value in enumerate(thread_list):
	#valuelist = [value, value, value]
	if idx==0:
		plt.plot(value, npdata[3*idx  ][0], color='r' ,marker='o', label='N = 2000 Real' )
		plt.plot(value, npdata[3*idx+1][0], color='b' ,marker='o', label='N = 4000 Real' )
		plt.plot(value, npdata[3*idx+2][0], color='g' ,marker='o', label='N = 8000 Real' )

		plt.plot(value, npdata[3*idx  ][1], color='r' ,marker='x', label='N = 2000 User' )
		plt.plot(value, npdata[3*idx+1][1], color='b' ,marker='x', label='N = 4000 User' )
		plt.plot(value, npdata[3*idx+2][1], color='g' ,marker='x', label='N = 8000 User' )	

		plt.plot(value, npdata[3*idx  ][2], color='r' ,marker='D', label='N = 2000 Sys' )
		plt.plot(value, npdata[3*idx+1][2], color='b' ,marker='D', label='N = 4000 Sys' )
		plt.plot(value, npdata[3*idx+2][2], color='g' ,marker='D', label='N = 8000 Sys' )	
	else:
		plt.plot(value, npdata[3*idx  ][0], color='r' ,marker='o' )
		plt.plot(value, npdata[3*idx+1][0], color='b' ,marker='o' )
		plt.plot(value, npdata[3*idx+2][0], color='g' ,marker='o' )

		plt.plot(value, npdata[3*idx  ][1], color='r' ,marker='x' )
		plt.plot(value, npdata[3*idx+1][1], color='b' ,marker='x' )
		plt.plot(value, npdata[3*idx+2][1], color='g' ,marker='x' )	

		plt.plot(value, npdata[3*idx  ][2], color='r' ,marker='D')
		plt.plot(value, npdata[3*idx+1][2], color='b' ,marker='D')
		plt.plot(value, npdata[3*idx+2][2], color='g' ,marker='D')	

plt.yscale('log')		
ymax = np.max(npdata)
plt.ylim(0, ymax)
#plt.legend(loc='best')
plt.legend(loc='upper left')
"""
xdata = npdata[0, 3, 5 ][ ]
ydata = 
plt.plot(xdata, ydata, label="N = 2000 "   )
"""

#Saves Plot
tmp_filename = "part1_time_plot.png"
plt.savefig(tmp_filename, rasterized=True)

print "The program has finished running. All files closed. \nThe results should be in your directory"



#End
