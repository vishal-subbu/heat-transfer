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


#dimen.nx = dimen.ny
#calculation of temp profile done for melt pool but properties used for solid material

def strip_casting(mold_temp,casting_speed,h,dimen, material):
	phase_profile = np.random.rand(dimen.npoints).reshape( (dimen.nx + 1, dimen.ny + 1, dimen.nz + 1))
	string= "./media/vishal/General1/Vishal_ubuntu/Additive_Manufacturing/All_functions/strip_casting/3_strip_casting"
	const = ((200*h*(mold_temp-material.melting_temp))/(casting_speed*material.density*material.heat_of_fusion*dimen.ny))
	phase_profile[:][:][:]=50
	z = dimen.nz/2
	y = dimen.ny/2
	fs=0
	theta1 = lambda t : const*t
	for i in range(dimen.nx+1):
		x = float(i)/100.0
		fs = const *x
		if fs<1:
			a = (np.sqrt(dimen.area*(1-fs)))*100.0
			y1 = int(y - (a/2))
			y2 = int(y + (a/2))
			z1 = int(z - (a/2))
			z2 = int(z + (a/2))
			for j in range(y1,y2+1):
				for k in range(z1,z2+1):
					phase_profile[i][j][k] = 100
		else :
			break
		print i , fs
	imageToVTK(string, cellData = None, pointData = {"phase" : phase_profile} )
	x = np.linspace(0.0,1.0,100)
	pl.plot(x,theta1(x))
	pl.grid(b =1)
	pl.show()

steel_1018 = material (1101 ,'steel' ,51.9, 787.0,571.791,1590.0,1260.0,10100000.0)
dimen_steel1018 = dimen (100,50,50,0.25,0.125)# dimen is in cm
strip_casting(2500.0,0.2,60.0,dimen_steel1018,steel_1018)


