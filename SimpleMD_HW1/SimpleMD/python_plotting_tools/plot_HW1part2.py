import sys
import os
import numpy as np
import matplotlib
matplotlib.use( 'Agg' )
import matplotlib.pyplot as plt

#FUNCTIONS
#-------------------------------------

def generatetreepointsA(scale, degeneracy):
    i=0
    newscale=[]
    newx=[]
    print("Did not Call function generatetreepoints")
    print("Scale 1: Len(scale1) = %d" % len(scale1))
    for element in scale:
	for j in xrange(0, int(degeneracy[i])):
            newscale.append(element)
	    newx.append(j+1)
	    j += 1            
	i += 1
    print("Length scale, x: %d, %d " % (len(newscale),len(newx)))
    return newscale, newx


def generatetreepointsA2(scale, degeneracy, degenmassses):
    i=0
    newscale=[]
    newx=[]
    newmasses = []
    print("Did Call function generatetreepoints")
    print("Scale 1: Len(scale) = %d" % len(scale))
    for element in scale:
	print element
	#print("Degeneracy[i] is: %d" %  degeneracy[i])
	#print("Degeneracy Mass is: %.1f" %  degenmasses[i])
        #print("len degeni degenmass:  %d  %d " % (len(degeneracy), len(degenmasses)))
	j = 0
	for j in xrange(0, int(degeneracy[i])+1):
	#for j in xrange(0, int(degeneracy[i])):   #experimental
            newscale.append(element)
            #newx.append(j+1)
            newx.append(j)
	    newmasses.append(degenmasses[j])
            j += 1            
        i += 1
    print("Length scale, x, masses: %d, %d  %d " % (len(newscale),len(newx), len(newmasses)))
    return newscale, newx, newmasses




def plottree(treeID, scale1, mass1, scaledegen, degenmasses,  cbcount):

    print "Called plottree"
    plot_title="Merger History Tree: %.0f Mass: %.1E" %  (float(treeID), mass1[0])  #Can code the number in with treem$
    x_axis="number of halos"
    y_axis="scale time"
    figure_name=os.path.expanduser('~/Nov18figureTreecolor%.0f.png' % float(treeID))
    
    #Choose which type of plot you would like: Commented out.
    scaledegennorm=[]
    masscolors=[]
    labels = []
    masses = []
    #Comment: If statement below is only to plot certain masses...
    #massminval = 1*10.0**11   #set low so it wont skip tree
    #massmaxval = 9*10.0**11  #For first halo. Only makes certain size halos. 	
    massminval = 10.0**0   #set low so it wont skip tree
    massmaxval = 10.0**30  #For first halo. Only makes certain size halos. 	
    if float(mass1[1])<massminval or float(mass1[1])>massmaxval:
	
	clearmass = []
        clearscale = []
        clearscaledegen =[]
	cleardegenmasses = []
	return clearmass, clearscale, clearscaledegen, cleardegenmasses	
    else:	
        ypoints, xpoints, masses= generatetreepointsA2(scale1, scaledegen, degenmasses)
	print("Generated x and y points and masses!")	

	plt.figure(figsize=(8,30))

	maxmass=max(masses)  #Max mass in entire masses
	print("Maxmass = %.2f" % maxmass)
	
	masscolorstr='none'
	i=0
	
	#'rgbcmykw'
	rval, gval, bval, cval, wval, kval, mval = 0.9999 , 0.99, 0.9, 0.8, 0.1, 0.01, 0.001
	labelvalues = [0.9999 , 0.99, 0.9, 0.8, 0.1, 0.01, 0.001]		

	for mass in masses:
		#masscolor = str(((mass/(maxmass))**(0.2))) #string for grey
		#masscolor = int(((mass/(maxmass))**(1))*99.0) #string for grey
		masscolor = ((mass/(maxmass))**(1)) #string for color

		#print masscolor

		if masscolor >= rval:
			masscolorstr = 'r'
			labelstr = "m/M = " + str(rval)	
		elif masscolor >= gval:
			labelstr = "m/M = " + str(gval)	
			masscolorstr = 'g'
		elif masscolor >= bval:
			labelstr = "m/M = " + str(bval)	
			masscolorstr = 'b'
		elif masscolor >= cval:
			labelstr = "m/M = " + str(cval)	
			masscolorstr = 'c'
		elif masscolor >= wval:
			labelstr = "m/M = " + str(wval)	
			masscolorstr = 'y'  #DONT USE WHITE. use yellow instead here
		elif masscolor >= kval:
			labelstr = "m/M = " + str(kval)	
			masscolorstr = 'k'
		elif masscolor >= mval or masscolor <mval:
			labelstr = "m/M = " + str(mval)	
			masscolorstr = 'm'

		masscolors.append(masscolorstr)
		labels.append(labelstr)
		
		#plt.scatter(xpoints[i],ypoints[i], s=25, c=masscolors[i], label=[i])
		#plt.scatter(xpoints[i],ypoints[i], s=25, c=masscolorstr, label=labelstr)
		i += 1
	elements = ['r','g','b','c','y','k','m']
	labelstring = "m/M= "
	currentlabel = ''
	
	jk = 0
	indexes = []
        xpointsplot = []
        ypointsplot = []
        masscolorsplot = []
	mergerplot = []
	mergerbool = []
	#Elemnts are the colors used for the plot
	for element in elements:
		l = 0   #This is used to track the indices which correspond to the mass fractions (Plot dot color)
		#print element, 
		indexes[:] = []
		xpointsplot[:] = []
		ypointsplot[:] = []
		masscolorsplot[:] = []
		mergerbool[:] = []     #tracks whether or not a specific event is a merger. 	
		for color in masscolors:
			if color == element:	
				#print ("%s : %s" % (element, color))
				indexes.append(l)
			l += 1
		print("len indexes is : %d" % len(indexes))

		for counter in indexes:
			xpointsplot.append(xpoints[counter])
			ypointsplot.append(ypoints[counter])
			masscolorsplot.append(masscolors[counter])
			#mergerplot.append(mergerbool[counter])
			
		#plt.scatter(xpoints[indexes],ypoints[indexes], s=25, c=masscolors[indexes])
		print "making label..."
		currentlabel = labelstring + " " +  str(labelvalues[jk])
		print currentlabel
		#good working plot statement below commented to experiment.
		#plt.scatter(xpointsplot,ypointsplot, s=15, c=masscolorsplot,edgecolor='', label = currentlabel, lw=1)
		plt.scatter(xpointsplot,ypointsplot, s=15, c=masscolorsplot,edgecolor='', label = currentlabel, lw=1)
		print "going to next iteraton"
		jk += 1



	print("mass colors determined")
	##############
	#plt.scatter(xpoints,ypoints, s=25, color=masscolors)
	#plt.scatter(xpoints,ypoints, s=10, edgecolor=None, color=masscolor, label="first tree")
	#plt.scatter(xpoints2,ypoints2, s=2, edgecolor=None, label="first tree")
	#Comment: For only ploting the color bar once
        
	plt.legend()
	plt.title(plot_title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
	#plt.xlim(0,max(newx))
	plt.xlim(0,max(xpoints))
	plt.ylim(0,1)

        print("About to save figure")
	plt.savefig(figure_name)

	print("Saving plot: %s" % figure_name)
        
	print("cbcount is %.0f" % float(cbcount))
	#In order to Plot only a single tree on a plot must clear lists before loop.
        #Comment out to over plot curves.
        #plt.clf()

        clearmass = []
        clearscale = []
        clearscaledegen =[]
	cleardegenmasses = []
        return clearmass, clearscale, clearscaledegen, cleardegenmasses
	#cleararray = []
	#return cleararray, cleararray, cleararray, cleararray


def plotdatatreecoloravg(treeID, scale1, mass1, scaledegen, cbcount):
    plot_title="Mass Accretion History Tree All trees"   #Can code the number in with treem$
    x_axis="scale time"
    y_axis="total mass"
    figure_name=os.path.expanduser('~/Nov9figureTreeaverage.png')
    #Choose which type of plot you would like: Commented out.
    scaledegennorm=[]
    #Comment: If statement below is only to plot certain masses...
    massminval = 10.0**11	
    if float(mass1[1])>massminval:
	clearmass = []
        clearscale = []
        clearscaledegen =[]
	print("Skipped halo because of mass")
	return clearmass, clearscale, clearscaledegen	
    else:	
	try:
		for scaled in scaledegen:
			poopvar=float(max(scaledegen))
			scaledegennorm.append(scaled/poopvar)
	except:
		print("Error reading in scale degeneracy value. Max(scaledegen)=%.2f " % poopvar)
  		print("Tree ID was: %f " % float(treeID))
		if poopvar == 0:
			#scaledegennorm.append(0, 0) 
			#print("Appended 1.0 to scaledgennorm")
			pass

	plt.scatter(scale1, mass1,c=scaledegennorm,s=1, edgecolor='none',alpha=0.5, label="first tree")
        #plt.plot(scale1, mass1, linestyle="-")
	#Comment: For only ploting the color bar once
	if cbcount == 100:
        	cb = plt.colorbar()
		cb.set_label("# of Neighboring Halos as fraction of local max", rotation=270)	

        plt.title(plot_title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
	plt.xlim(0,1)
	plt.yscale("log")
	
	#Comment: Uncomment to plot the colorbar only for the finial halos. 
	#if cbcount > (400.0-10): 
        #	plt.savefig(figure_name)
	#        print("Saving plot: %s" % figure_name)
 	plt.savefig(figure_name)
        print("Saving plot: %s" % figure_name) 

        print("cbcount is %.0f" % float(cbcount))
	#In order to Plot only a single tree on a plot must clear lists before loop.
        #Comment out to over plot curves.
        #plt.clf()

        clearmass = []
        clearscale = []
        clearscaledegen =[]

        return clearmass, clearscale, clearscaledegen




def plotdatatreecolor(treeID, scale1, mass1, scaledegen):
        plot_title="Mass Accretion History Tree " + str(treeID)   #Can code the number in with treemax
        x_axis="scale time"
        y_axis="total mass"
        figure_name=os.path.expanduser('~/figureTree' + str(treeID)+'.png')
        #Choose which type of plot you would like: Commented out.
        plt.scatter(scale1, mass1,c=scaledegen, edgecolor='none', label="first tree")
        plt.plot(scale1, mass1, linestyle="-")
	
	cb = plt.colorbar()
	
        plt.title(plot_title)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        #plt.yscale("log")

        plt.savefig(figure_name)
        print("Saving plot: %s" % figure_name)
        print
	#In order to Plot only a single tree on a plot must clear lists before loop.
        #Comment out to over plot curves.
        plt.clf()

        clearmass = []
        clearscale = []
	clearscaledegen =[]

        return clearmass, clearscale, clearscaledegen



def plotdatatree(treeID, scale1, mass1):
	plot_title="Mass Accretion History Tree " + str(treeID)   #Can code the number in with treemax
	x_axis="scale time"
	y_axis="total mass"
	figure_name=os.path.expanduser('~/figureTree' + str(treeID)+'.png')
	#Choose which type of plot you would like: Commented out.
	plt.plot(scale1, mass1, linestyle="-", marker="o")
	#plt.scatter(scale1, mass1, label="first tree")
	
	
	plt.title(plot_title)
	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#plt.yscale("log")

	plt.savefig(figure_name)
	print("Saving plot: %s" % figure_name)
	print
	#In order to Plot only a single tree on a plot must clear lists before loop. 
	#Comment out to over plot curves.			
	plt.clf()

	clearmass = []
	clearscale = []

	return clearmass, clearscale

def checktreemax(totaltrees, treemax):
	if totaltrees >= treemax:
        	print("Totaltrees > treemax")
         	return True
	else:
		return False

def checkmaxiteration(icount, maxiteration1):
	if icount > maxiteration1:
                print("maxiterations reached!")
                print("Set iterations higher or reduce data!")
                print("Breaking Loop... ... ...")
                return True
	else:
		return False


def setUSEtreeIDlist(treeIDlist):
	if len(treeIDlist)>0:
		print "setting USEtreeIDlist to 1"
		USEtreeIDlist = 1  #set to 0 to ignore specified trees. 1 to start at treeIDlist[0] 
	else:
		USEtreeIDlist = 0

	return USEtreeIDlist


def printmassdifferences(scaleID, scale_previous,  mass_previous, massval, massdiffval, scalecount):
	print
	print("FOUND A LARGER MASS AT SAME SCALE! what should i do????")
	print("Scale %d |  scale_prev |    Mass Previous   |    Mass Current    |    massdiff" % (scalecount))
	print(" %.5f  |   %.5f   |     %.2E       |     %.2E       |    %.3E" % \
			 (scaleID, scale_previous,  mass_previous, massval, massdiffval))  
	return 0

