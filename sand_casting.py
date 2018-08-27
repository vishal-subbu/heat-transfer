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


def sand_casting(mold_temp,step_count,h,dimen, material,mold_material):
	phase_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/sand_casting/1_sand_casting"
	a = (2/(np.sqrt(np.pi)))
	b = ((material.melting_temp-mold_temp)/(material.density*material.heat_of_fusion))
	c = (np.sqrt(mold_material.thermal_conductivity*mold_material.density*mold_material.specific_heat))
	d = a*b*c
	m=0
	X =0
	theta1 = lambda t : d*np.sqrt(t)
	phase_profile[:][:][:]=100
	t =0.0
	X = d*np.sqrt(t)
	filename=string+str(m)
	print a , b , c , d
	while X<1:		
		i = int( X * dimen.nx )
		phase_profile[0:i][:][:] = 50
		print t , X
		imageToVTK(filename, cellData = None, pointData = {"phase" : phase_profile} )
		m =m +1
		filename=string+str(m)
		phase_profile[:][:][:]=100
		t =t +step_count
		X = d*np.sqrt(t)
	x = np.linspace(0.0,40,100)
	pl.plot(x,theta1(x))
	pl.grid(b =1)
	pl.show()


# mold properties has to be added

steel_1018 = material (1101 ,'steel' ,51.9, 787.0,571.791,1590.0,9600.0,10100000.0)
dimen_steel1018 = dimen (50,10,10,0.05,0.05)#in cm
sillica = material (1105 ,'sillica' ,0.6, 1500,1160,1590.0,96000.0,10100000.0)
sand_casting(500.0,1.0,20.0,dimen_steel1018,steel_1018,sillica)


