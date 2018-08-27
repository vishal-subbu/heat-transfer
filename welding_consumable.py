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

def Welding_Consumble_electrode(initial_temp,feed_rate,dimen, material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/Welding_consumable/Welding_consumable_electrode_2"
	l = np.exp(feed_rate*(dimen.nx/100.0)/material.alpha)
	for i in range (dimen.nx+1):
		x = float(i)/100.0
		theta = (np.exp(feed_rate*x/material.alpha)-1)/(l-1)
		temp=initial_temp + (material.melting_temp - initial_temp)*(theta)
		temp_profile[i][:][:] = temp
		print i, theta
	imageToVTK(string, cellData = None, pointData = {"temp" : temp_profile} )


steel_1018 = material (1101 ,'steel' ,51.9, 7870.0,571.791,1590.0,96000.0,10100000.0)
dimen_steel1018 = dimen (50,10,10,0.05,0.05)#in cm
Welding_Consumble_electrode(27.0,0.000461,dimen_steel1018,steel_1018)




