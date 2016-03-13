import sys
import numpy as np
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#THIS PROGRAM PLOTS DATA IN FORM 'x, y'

#fig=plt.figure(figsize=(10,5))

#f2 = open('time_stats_run1temp.txt' , "r")

filename = 'time_stats_run1.txt'
#with open('time_stats_run1temp.txt' , "r") as f2:
thread_list = [1, 4, 8, 16, 32]
N_size_list = [2000, 4000, 8000]

#for line in f2:
npdata = np.loadtxt(filename)

print npdata 
print
print npdata[1]
print 
print npdata[1][1]


xdata = []
ydata1 = []
ydata2 = []
ydata3 = []

print("Data should be structured (Real, User, Sys)...")

plot_title="Real Time vs. # of Threads "
x_axis="Number of Threads "
y_axis="Time [sec] "

plt.title(plot_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
"""
for idx, value in enumerate(thread_list):
	#valuelist = [value, value, value]
	print("idx: %d " % idx)
	print npdata[3*idx][2]
	if idx==0:		
		plt.plot(value, npdata[3*idx+2][0], color='g' ,marker='o', label='N = 8000 Real' )
		plt.plot(value, npdata[3*idx+1][0], color='b' ,marker='o', label='N = 4000 Real' )
		plt.plot(value, npdata[3*idx  ][0], color='r' ,marker='o', label='N = 2000 Real' )

	else:
		plt.plot(value, npdata[3*idx  ][0], color='r' ,marker='o' )
		plt.plot(value, npdata[3*idx+1][0], color='b' ,marker='o' )
		plt.plot(value, npdata[3*idx+2][0], color='g' ,marker='o' )
"""
#---------------
indexes1 = [3*i     for i in range(0,len(thread_list)) ]
indexes2 = [3*i+1   for i in range(0,len(thread_list)) ]
indexes3 = [3*i+2   for i in range(0,len(thread_list)) ]

#print indexes1 
#REAL TIME
for i in range(0, len(thread_list)):
	ydata1.append( npdata[indexes1[i]][0] )
	ydata2.append( npdata[indexes2[i]][0] )
	ydata3.append( npdata[indexes3[i]][0] )

plt.plot(thread_list, ydata3, color='g' ,marker='o', label='N = 8000 Real' )
plt.plot(thread_list, ydata2, color='b' ,marker='o', label='N = 4000 Real' )
plt.plot(thread_list, ydata1, color='r' ,marker='o', label='N = 2000 Real' )
ydata1[:] = []
ydata2[:] = []
ydata3[:] = []


#---------------

"""
len_threads = len(thread_list)
indexes1 = [3*i   for i in range(0,len_threads) ]
indexes2 = [3*i+1 for i in range(0,len_threads) ]
indexes3 = [3*i+2 for i in range(0,len_threads) ]

data1 = npdata[indexes1 ][0]
data2 = npdata[indexes2 ][0]
data3 = npdata[indexes3 ][0]

plt.plot(thread_list, npdata[indexes1 ][0],linestyle='-', color='r' ,marker='o', label='N = 2000 Real' )
plt.plot(thread_list, npdata[indexes2 ][0],linestyle='-', color='r' ,marker='o', label='N = 4000 Real' )
plt.plot(thread_list, npdata[indexes3 ][0],linestyle='-', color='r' ,marker='o', label='N = 8000 Real' )
"""
	
plt.ylim(0, 1400)	
plt.legend(loc='best')

"""
xdata = npdata[0, 3, 5 ][ ]
ydata = 
plt.plot(xdata, ydata, label="N = 2000 "   )
"""

#Saves Plot
tmp_filename = "part1_time_plotREAL.png"
plt.savefig(tmp_filename, rasterized=True)
plt.clf()


plot_title="User Time vs. # of Threads "
x_axis="Number of Threads "
y_axis="Time [sec] "
plt.title(plot_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

"""
for idx, value in enumerate(thread_list):
	#valuelist = [value, value, value]
	if idx==0:
		plt.plot(value, npdata[3*idx+2][1], color='g' ,marker='x', label='N = 8000 User' )	
		plt.plot(value, npdata[3*idx+1][1], color='b' ,marker='x', label='N = 4000 User' )
		plt.plot(value, npdata[3*idx  ][1], color='r' ,marker='x', label='N = 2000 User' )
		
	else:
		plt.plot(value, npdata[3*idx  ][1], color='r' ,marker='x' )
		plt.plot(value, npdata[3*idx+1][1], color='b' ,marker='x' )
		plt.plot(value, npdata[3*idx+2][1], color='g' ,marker='x' )	
		
"""

#USER TIME
for i in range(0, len(thread_list)):
	ydata1.append( npdata[indexes1[i]][1] )
	ydata2.append( npdata[indexes2[i]][1] )
	ydata3.append( npdata[indexes3[i]][1] )

plt.plot(thread_list, ydata3, color='g' ,marker='x', label='N = 8000 User' )
plt.plot(thread_list, ydata2, color='b' ,marker='x', label='N = 4000 User' )
plt.plot(thread_list, ydata1, color='r' ,marker='x', label='N = 2000 User' )
ydata1[:] = []
ydata2[:] = []
ydata3[:] = []


plt.ylim(0, 2500)	

plt.legend(loc='best')
"""
xdata = npdata[0, 3, 5 ][ ]
ydata = 
plt.plot(xdata, ydata, label="N = 2000 "   )
"""

#Saves Plot
tmp_filename = "part1_time_plotUSER.png"
plt.savefig(tmp_filename, rasterized=True)
plt.clf()


plot_title="System Time vs. # of Threads "
x_axis="Number of Threads "
y_axis="Time [sec] "
plt.title(plot_title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

"""
for idx, value in enumerate(thread_list):
	#valuelist = [value, value, value]
	if idx==0:
		s3 = plt.plot(value, npdata[3*idx+2][2], linestyle='-.', color='g' ,marker='D', label='N = 8000 Sys' )	
		s2 = plt.plot(value, npdata[3*idx+1][2], linestyle='--', color='b' ,marker='D', label='N = 4000 Sys' )
		s1 = plt.plot(value, npdata[3*idx  ][2], linestyle='-', color='r' ,marker='D', label='N = 2000 Sys' )
	
	else:
		s1 = plt.plot(value, npdata[3*idx  ][2], linestyle='-', color='r' ,marker='D')
		s2 = plt.plot(value, npdata[3*idx+1][2], linestyle='--', color='b' ,marker='D')
		s3 = plt.plot(value, npdata[3*idx+2][2], linestyle='-.', color='g' ,marker='D')	
"""
#SYS TIME
for i in range(0, len(thread_list)):
	ydata1.append( npdata[indexes1[i]][2] )
	ydata2.append( npdata[indexes2[i]][2] )
	ydata3.append( npdata[indexes3[i]][2] )

plt.plot(thread_list, ydata3, color='g' ,marker='D', label='N = 8000 Real' )
plt.plot(thread_list, ydata2, color='b' ,marker='D', label='N = 4000 Real' )
plt.plot(thread_list, ydata1, color='r' ,marker='D', label='N = 2000 Real' )
ydata1[:] = []
ydata2[:] = []
ydata3[:] = []


plt.ylim(0, 0.9)	
	
plt.legend(loc='best')
"""
xdata = npdata[0, 3, 5 ][ ]
ydata = 
plt.plot(xdata, ydata, label="N = 2000 "   )
"""

#Saves Plot
tmp_filename = "part1_time_plotSYS.png"
plt.savefig(tmp_filename, rasterized=True)
plt.clf()

print "The program has finished running. All files closed. \nThe results should be in your directory"



#End