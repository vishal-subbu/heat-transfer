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

def welding_thick_plate(initial_temp,heat_input,velocity,dimen,material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/welding_thick_plate/welding_thick_plate_test_1_6.2"
	l = ((heat_input)/(2*np.pi*material.thermal_conductivity))
	expo = (velocity/(2*material.alpha))
	x = 0.0
	y = 0.0
	for i in range (dimen.nx+1):
		x = float(i-50) / 1000.0
		for j in range (dimen.ny+1):
			y = float(j-24) / 1000.0
			for k in range (dimen.nz+1):
				z = float (k)/1000.0
				r= np.sqrt((x**2)+(y**2)+(z))
				if r == 0.0 :
					r = 0.001		 
				temp_profile[i][j][k] = ((l/r)*np.exp(expo*(x-r))) + initial_temp
			print i, j ,k, temp_profile[i][j][k]
	print np.amax(temp_profile), np.amin(temp_profile)
	imageToVTK(string, cellData = None, pointData = {"temp" : temp_profile} )



steel_1018 = material (1101 ,'steel' ,51.9, 7870.0,571.791,1590.0,96000.0,10100000.0)
dimen_steel1018 = dimen (100,50,10,0.05,0.05)# dimen is in cm
welding_thick_plate(25.0,5000,0.0062,dimen_steel1018,steel_1018)


