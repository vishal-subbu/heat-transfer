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



def Spot_laser_welding(initial_temp,heat_input,final_time,time_step,dimen,material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/spot_laser_steel/Spot_laser_welding_steel_test1"
	t =0.0
	m=0
	x1 =dimen.nx/2
	y1 = dimen.ny/2
	t =time_step/2
	while t < final_time:
		filename=string+str(m)
		for i in range (dimen.nx+1):
			x =float(i)/1000.0
			for j in range (dimen.ny+1):
				y =float(j)/1000.0
				for k in range (dimen.nz+1):
					z =float(k)/1000.0
					l = ((((x-x1)**2)+((y-y1)**2)+(z**2))/(4*material.alpha*t))
					exponen = np.exp((-1.0)*l)
					a = 2*heat_input
					b = material.density*material.specific_heat
					c = ((4*np.pi*material.alpha*t)**1.5)
					temp_profile[i][j][k]=initial_temp + ((a/(b*c))*exponen)
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		print t ,np.amax(temp_profile),np.amin(temp_profile) 
		t = t +time_step
		m= m+1



steel_1018 = material (1101 ,'steel' ,51.9, 7870.0,571.791,1590.0,96000.0,10100000.0)
dimen_steel1018 = dimen (100,50,1,0.05,0.05)# dimen is in cm
Spot_laser_welding(25.0,5000,5,0.01,dimen_steel1018,steel_1018)



