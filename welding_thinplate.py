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
from scipy.special import kn
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

def welding_thin_plate(initial_temp,heat_input,velocity,dimen,material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/welding_thin_plate/welding_thin_plate_6.2"
	l = ((heat_input*1000.0)/(4*np.pi*material.thermal_conductivity*dimen.nz))
	expo = (velocity/(2*material.alpha))
	for i in range (dimen.nx+1):
		x = float(i-50) / 1000.0
		for j in range (dimen.ny+1):
			y = float(j-30) / 1000.0
			for k in range (dimen.nz+1):
				r= np.sqrt((x**2)+(y**2))	
				if r == 0.0:
					r  = 0.001
				temp_profile[i][j][k] = (l*np.exp(expo*x)*kn(0,expo*r))+ initial_temp
	imageToVTK(string, cellData = None, pointData = {"temp" : temp_profile} )

#                 code, category , thermal_conductivity , density , specific_heat, melting_temp, heat_of_fusion,elecric_conductivity

alum = material (1103 ,'aluminium' ,229, 2700.0,1000.0,660.0,96000.0,10100000.0)
dimen_alum = dimen (100,100,32,0.05,0.05)# dimen is in cm
welding_thin_plate(25.0,1000,0.0062,dimen_alum,alum)





