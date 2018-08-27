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



def ierfc(z):
	a = np.exp((-1)*(z**2))/(np.sqrt(np.pi))
	b = z- (z*erf(z))
	return a-b



#calculation of temp profile done for melt pool but properties used for solid material

def uniform_surface_heating(initial_temp,heat_input,t_on,final_time,step_count,dimen,material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/uniform_surfacce_heating/uniform_surface_heating"
	l = (2*heat_input*(np.sqrt(material.alpha)))/material.thermal_conductivity
	n =0
	t = step_count/2
	while t  < t_on:
		filename = string + str(n)
		m = np.sqrt(4*material.alpha*t)
		for i in range(dimen.nx+1):
			x = float(i) / 1000.0
			temp_profile[i][:][:] = initial_temp + l*np.sqrt(t)*(ierfc(x/m))
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		n = n+1
		t = t + step_count

	while t  < final_time:
		filename = string + str(n)
		m1 = np.sqrt(4*material.alpha*t)
		m2 = np.sqrt(4*material.alpha*(t-t_on))
		for i in range(dimen.nx+1):
			x = float(i) / 1000.0
			c = np.sqrt(t)*ierfc(x/m1)
			d = np.sqrt(t-t_on)*ierfc(x/m2)
			temp_profile[i][:][:] = initial_temp + l*(c- d)
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		n = n+1
		t = t + step_count


#                 code, category , thermal_conductivity , density , specific_heat, melting_temp, heat_of_fusion,elecric_conductivity

alum = material (1103 ,'aluminium' ,229, 2700.0,1000.0,660.0,96000.0,10100000.0)
dimen_alum = dimen (100,100,32,0.05,0.05)# dimen is in cm
uniform_surface_heating(25.0,10000,10.0,20.0,0.1,dimen_alum,alum)





