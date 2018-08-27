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
from scipy.optimize import fsolve
import numpy as np 
import math

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



def Bulk_heating(final_temp,initial_temp,final_time,step_count,h, dimen, material):
	temp_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General/Vishal_ubuntu/Additive_Manufacturing/All_functions/Bulk_heating/Bulk_heating"
	biot = (h * dimen.nx )/(2000*material.thermal_conductivity)
	roots = np.zeros(5)
	a = np.zeros(5)
	b = np.zeros(5)		
	m1 = 0
	l = float(dimen.nx)/1000.0
	print l
	t = 0.0
	solve  = lambda x : (x*math.tan(x*np.pi/180.0)) - biot
	roots[0] = fsolve (solve,1)
	roots[1] = fsolve (solve,180)
	roots[2] = fsolve (solve,360)
	roots[3] = fsolve (solve,540)
	roots[4] = fsolve (solve,720)
	print roots
	for i in range(5):
		a[i] = math.sin(roots[i]*np.pi/180.0)/(roots[i] + (math.sin(roots[i]*np.pi/180.0)*math.cos(roots[i]*np.pi/180.0)))
	print a
	while t<=final_time:
		filename=string+str(m1)
		f0 = (material.alpha*t*1000000)/(dimen.nx*dimen.nx)
		for j in range(5):
			b[j] = np.exp((-1)*roots[j]*roots[j]*f0)
		for i in range (dimen.nx+1):
			x  =float(i)/1000.0
			sum_root =0.0;
			for k in range (5):
				sum_root = sum_root + a[k]*b[k]*math.cos(roots[k]*x*np.pi/(l*180.0))
			theta = 2* sum_root
			print t , i , theta
			temp=final_temp +  (initial_temp-final_temp)*theta
			temp_profile[i][:][:]=temp
		imageToVTK(filename, cellData = None, pointData = {"temp" : temp_profile} )
		print t,np.amax(temp_profile),np.amin(temp_profile)
		t = t + step_count
		m1=m1+1
	



steel_1018 = material (1101 ,'steel' ,51.9, 7870.0,571.791,1590.0,96000.0,10100000.0)
dimen_steel1018 = dimen (200,10,10,0.05,0.05)# dimen is in mm
Bulk_heating(27.0,1000.0,0.001,0.0001,10.0,dimen_steel1018,steel_1018 )

