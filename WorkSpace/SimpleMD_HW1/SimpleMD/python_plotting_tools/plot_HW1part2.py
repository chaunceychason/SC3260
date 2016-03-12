import sys
import os
import numpy as np
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt

#FUNCTIONS
#-------------------------------------
def plotfunc(xpoints, ypoints):

    print "Called plotfunc"
    plot_title="FLOPS in energy function vs. # Atoms"
    x_axis="number of atoms"
    y_axis="number of FLOPS"
    figure_name=os.path.expanduser('~/Feb7HW1Part2B.png')
    

    #plt.figure(figsize=(8,30))

    plt.scatter(xpoints,ypoints, s=15, label="")
        
    #plt.legend()
    plt.title(plot_title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    #plt.xlim(0,max(newx))
    #plt.xlim(0,max(xpoints))
    #plt.ylim(0,160)
    plt.yscale('log')

    print("About to save figure")
    plt.savefig(figure_name)

    print("Saving plot: %s" % figure_name)
        
    #plt.clf()

    return 0


#BEGIN MAIN FUNCTION


filename = 'datafile1.txt'
with open(filename) as fn:
    atomarray = []
    timearray = []
    floparray = []
    for line in fn:
        #poop = fn.readline()
	try:
            atom_num, time_num, flop_num = line.split()
            print atom_num, time_num, flop_num
	    atomarray.append(atom_num)
	    timearray.append(time_num)
	    floparray.append(flop_num)
	except:
	    continue


print("Finished running")
plotfunc(atomarray, floparray)
