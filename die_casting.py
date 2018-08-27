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


def die_casting(mold_temp,step_count,h,dimen, material):
	phase_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/die_casting/die_casting"
	s  = (h*(material.melting_temp - mold_temp))/(material.density*material.heat_of_fusion)
	m=0
	X =0
	theta1 = lambda t : (h*t*(material.melting_temp - mold_temp))/(material.density*material.heat_of_fusion)
	phase_profile[:][:][:]=100
	t = (step_count)/2
	X = s*t
	filename=string+str(m)
	while X<1:		
		i = int( X * dimen.nx )
		phase_profile[0:i][:][:] = 50
		print t , X
		imageToVTK(filename, cellData = None, pointData = {"phase" : phase_profile} )
		m =m +1
		filename=string+str(m)
		phase_profile[:][:][:]=100
		t =t +step_count
		X = s*t
	x = np.linspace(0.0,1.0,100)
	pl.plot(x,theta1(x))
	pl.grid(b =1)
	pl.show()



iron = material (1100 ,'iron' ,80000.0, 0.008,0.450,1590.0,96000.0,10100000.0)
dimen_iron = dimen (200,200,200,400.0,80000000.0)
die_casting(500.0,0.001,20.0,dimen_iron,iron)


