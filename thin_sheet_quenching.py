#
# Copyright (c) 2018, Vishal_S
# All rights reserved. Please read the "license.txt" for license terms.
#
# Project Title: Heat transfer during welding
#
# Developer: Vishal S
#
# Contact Info: vishalsubbu97@gmail.com
#
from evtk.hl import imageToVTK
from scipy.special import erf

import numpy as np 
import pylab as pl

def writenumpytovtk(dimen,temp):
        fo = open("","w")
        fo.write("# vtk DataFile Version 2.0\n")
        fo.write("Data CFD code\n")
        fo.write("ASCII\n")
        fo.write("DATASET RECTILINEAR_GRID\n")
        fo.write("DIMENSIONS %d %d %d\n" %dimen.nx %dimen.ny %dimen.nz)
        fo.write("X_COORDINATES %d float\n " %dimen.nx)
        for i in range(dimen.nx):
                x = float(i/1000)
                f.wrtie ("%f "%x)
        fo.write("\nY_COORDINATES %d float\n " %dimen.ny)
        for i in range(dimen.ny):
                y = float(i/1000)
                f.wrtie ("%f "%y)
        fo.write("\nZ_COORDINATES %d float\n " %dimen.nz)
        for i in range(dimen.nz):
                z = float(i/1000)
                f.wrtie ("%f "%z)                
class material :
	def __init__ (self, code, category , thermal_conductivity , density , specific_heat, melting_temp, heat_of_fusion,elecric_conductivity):
		self.code=code
		self.category = category
		self.thermal_conductivity=thermal_conductivity
		self.density=density
		self.specific_heat=specific_heat
		self.melting_temp=melting_temp
		self.alpha=(thermal_conductivity)/(density*specific_heat)
		self.heat_of_fusion = heat_of_fusion
		self.elecric_conductivity=elecric_conductivity



class dimen :
	def __init__(self,nx,ny,nz,area,volume):
		self.nx=nx
		self.ny=ny
		self.nz=nz
		self.area=area
		self.volume=volume
		self.npoints = (nx+1)*(ny+1)*(nz+1)



def Quenching_of_thin_sheet(final_temp,initial_temp,final_time,step_count,h, dimen, material):
	mass = dimen.volume*material.density
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/thin_sheet/1_thin_sheet_quenching_2"
	m=0
	t=0.0
	theta1 = lambda t : np.exp((-1.0*dimen.area*t)/(mass*material.specific_heat))
	while t<=final_time:
		filename=string+str(m)
		theta = np.exp((-1.0*dimen.area*t)/(mass*material.specific_heat))
		temp=final_temp +  (initial_temp-final_temp)*theta
		temp_profile[:][:][:]=temp
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		print t,np.amax(temp_profile),np.amin(temp_profile)
		t = t + step_count
		m=m+1
	x = np.linspace(0.0,0.01,100)
	pl.plot(x,theta1(x))
	pl.grid(b =1)
	pl.show()




iron = material (1100 ,'iron' ,80000.0, 0.008,0.450,1590.0,96000.0,10100000.0)
dimen_iron = dimen (20,20,1,400.0,400.0)
Quenching_of_thin_sheet(27.0,1000.0,0.01,0.0001,10,dimen_iron,iron)

