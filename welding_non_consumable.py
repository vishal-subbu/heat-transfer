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


def Welding_Non_consumable_electrode(final_temp,initial_temp,current_density, dimen, material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/Welding_non_consumable/1_Welding_Non_consumable_electrode_"
	s = (current_density)**2/(material.elecric_conductivity)
	l =float(dimen.nx)/1000.0
	for i in range (dimen.nx+1):
		x = float(i)/1000.0
		temp=initial_temp + ((s*x*(l-x))/(2*material.thermal_conductivity)) + x*(final_temp-initial_temp)/(l)
		temp_profile[i][:][:] = temp
		print i, temp_profile[i][0][0] 
	imageToVTK(string, cellData = None, pointData = {"temp" : temp_profile} )



tungsten = material (1101 ,'steel' ,175.0, 19250.0,135.0,3422.0,46000.0,18939393.94)
dimen_tungsten = dimen (20,2,2,0.000004,0.05)#in mm
Welding_Non_consumable_electrode(3500,2500.0,75000000.0,dimen_tungsten,tungsten)



