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




def integration(t,i,j,k,velocity,radius_of_heat_source,y,material):
	if t == 0:
		return 0
	else :
		denom1 = (4*material.alpha*t)
		denom2 = (radius_of_heat_source**2)
		denom = (denom1 + denom2)*(np.sqrt(t))
		num1  = ((i-(velocity*t))**2)+((j-y)**2)
		num  =  ((num1/(denom1+denom2))+((k**2)/(denom1)))
		exponen = np.exp((-1.0)*(num))
		return (exponen/denom)



def Scanning_laser_welding(initial_temp,heat_input,final_time,time_step,velocity,radius_of_heat_source,dimen,material):
	temp_profile_new = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	temp_profile_old = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	temp_profile_old[:][:][:] = initial_temp
	temp_profile_new[:][:][:] = initial_temp*2
	
	constant  = (heat_input)/(material.density*material.specific_heat*(np.pi**1.5)*(material.alpha**0.5))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/scan_laser_steel/Scanning_laser_welding_2_2d_test"
	m=0
	t = 0.0
	y1 = float(dimen.ny)/2000.0
	while t<=final_time:
		filename=string+str(m)
		t_dash = t + time_step
		for i in range (dimen.nx+1):
			x = float (i)/1000.0
			for j in range (dimen.ny+1):
				y = float (j)/1000.0
				for k in range (dimen.nz+1):
					z = float (k)/1000.0
					integ1 = (integration(t,x,y,z,velocity,radius_of_heat_source,y1,material))
					integ2 = (integration(t_dash,x,y,z,velocity,radius_of_heat_source,y1,material))
					integ = ((integ1+integ2)/2)
					temp_profile_new[i][j][k] = (constant*integ*time_step) + temp_profile_old[i][j][k]
					print t,i,j,k,integ1,integ2
		print t,np.amax(temp_profile_new),np.amin(temp_profile_new)
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile_new} )
		temp_profile_old = temp_profile_new 
		t = t + (time_step)
		m=m+1

	






steel_1018 = material (1101 ,'steel' ,51.9, 7870.0,571.791,1590.0,96000.0,10100000.0)
dimen_steel1018 = dimen (50,50,0,0.05,0.05)# dimen is in cm
Scanning_laser_welding(27.0,5000,10.0,0.1,0.01,0.001,dimen_steel1018,steel_1018)






