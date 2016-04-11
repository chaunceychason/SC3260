import sys
import numpy as np
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#THIS PROGRAM PLOTS DATA IN FORM 'x, y'

filename = 'time_stats_run1.txt'
#with open('time_stats_run1temp.txt' , "r") as f2:
#thread_list = [16]
#N_size_list = [2000, 4000, 8000]
run_list = [125, 500, 1000, 2000, 4000 ]

#DATA STRUCTURE
#for line in f2:
#REAL,  USER,  SYS 
#125
#500
#1000
#2000
#4000

npdata = np.loadtxt(filename)

xdata = []
ydata1 = []
#ydata2 = []
#ydata3 = []

print("Data should be structured (Real, User, Sys)...")

"""
=====================================
         REAL TIME  PLOT 
=====================================
"""


plot_title="Real Time vs. System Size "
x_axis="System Size "
y_axis="Real Time [sec] "

plt.title(plot_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

#---------------
indexes1 = [i     for i in range(0,len(run_list)) ]
#indexes2 = [3*i+1   for i in range(0,len(thread_list)) ]
#indexes3 = [3*i+2   for i in range(0,len(thread_list)) ]

#print indexes1 
#REAL TIME
for i in range(0, len(run_list)):
	ydata1.append( npdata[indexes1[i]][0] )
	#ydata2.append( npdata[indexes2[i]][0] )
	#ydata3.append( npdata[indexes3[i]][0] )

#Real_Times = [ydata1, ydata2, ydata3 ]

#plt.plot(thread_list, ydata3, color='g' ,marker='o', label='N = 8000 Real' )
#plt.plot(thread_list, ydata2, color='b' ,marker='o', label='N = 4000 Real' )
plt.plot(run_list, ydata1, color='r' ,marker='o', label='Real Times' )
ydata1[:] = []
#ydata2[:] = []
#ydata3[:] = []


#---------------	
#plt.ylim(0, 1400)	
plt.legend(loc='best')

#Saves Plot
tmp_filename = "part2_time_plotREAL.png"
plt.savefig(tmp_filename, rasterized=True)
plt.clf()







print "The program has finished running. All files closed. \nThe results should be in your directory"



#End
