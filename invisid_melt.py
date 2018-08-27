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


#calculation of temp profile done for melt pool but properties used for solid material

def Invisid_melt_spinning(initial_temp,feed_rate,dimen,material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/invisid_melt_spinning/4_Invisid_melt_spinning"
	l = ((material.heat_of_fusion/(material.specific_heat*(material.melting_temp- initial_temp)))+1)
	print l, material.alpha
	for i in range (dimen.nx+1):
		x = float(i)/1000.0
		theta = (np.exp((feed_rate*x)/material.alpha)-1)*(l)
		temp=initial_temp + (material.melting_temp - initial_temp)*(theta)
		temp_profile[i][:][:] = temp
		print i, temp_profile[i][0][0], theta
	imageToVTK(string, cellData = None, pointData = {"temp" : temp_profile} )


#  code, category , thermal_conductivity , density , specific_heat, melting_temp, heat_of_fusion,elecric_conductivity)

liquid_iron = material (1100 ,'iron' ,43.725, 6586.605,825,1590.0,96000.0,627035.2298)
dimen_liquid_iron = dimen (13,20,20,400.0,80000000.0)
Invisid_melt_spinning(2500.0,0.000461,dimen_liquid_iron,liquid_iron)


