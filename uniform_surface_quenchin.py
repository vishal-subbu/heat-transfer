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

def Uniform_Surface_heating(final_temp,initial_temp,final_time,step_count,h, dimen, material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/Uniform_surface_quenching/1_Uniform_Surface_quenching"
	m=0
	l = 2.0
	theta1 = lambda t : erf(l) + (np.exp(t + (t*t/(4*l*l))))*(1-erf(t + t/(2*l)))
	t = (step_count)/2
	while t<=final_time:
		filename=string+str(m)
		for i in range (dimen.nx+1):
			filename=string+str(m)
			a = (float(i))/(np.sqrt(4*material.alpha*t))
			b = h*i/material.thermal_conductivity
			c = ((h**2)*(material.alpha)*t)/(material.thermal_conductivity**2)
			d = np.sqrt(c)
			theta = erf(a) + (np.exp(b+c)*(1-erf(a+d)))
			temp=final_temp +  (initial_temp-final_temp)*theta
			temp_profile[i][:][:]=temp
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		print t,np.amax(temp_profile),np.amin(temp_profile)
		t = t + step_count
		m=m+1
	x = np.linspace(0.0,1.0,100)
	pl.plot(x,theta1(x))
	pl.grid(b =1)
	pl.show()



iron = material (1100 ,'iron' ,80000.0, 0.008,0.450,1590.0,96000.0,10100000.0)
dimen_iron = dimen (2000,10,10,400.0,400.0)
Uniform_Surface_heating(27.0,1000.0,2.0,0.001,10,dimen_iron,iron)

