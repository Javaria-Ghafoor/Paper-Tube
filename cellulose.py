from vpython import *
from vpython import sphere
from numpy import *
from math import *

atoms = []


def sph2cart(r, theta, phi):
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return vector(x, y, z)


mC = 1.9944235 * 10**(-26)  # kg
mH = 1.6735575 * 10**(-27)  # kg
mO = 2.6566962 * 10**(-26)  # kg
rC = 1.7 * 10**(-10)  # m
rH = 1.2 * 10**(-10)  # m
rO = 1.52 * 10**(-10)  # m
C_H = 1.09 * 10**(-10)  # m
C_O = 1.43 * 10**(-10)  # m
O_H = 0.96 * 10**(-10)  # m
C_C = 1.54 * 10**(-10)  # m

C1 = sphere(pos=vector(0, 0, 0), radius=rC, color=color.yellow, mass=mC)
H1 = sphere(pos=C1.pos+sph2cart(C_H, 0, 0), radius=rH, color=color.blue, mass=mH)
O11 = sphere(pos=C1.pos+sph2cart(C_O, deg2rad(109.5), 0), radius=rO, color=color.green, mass=mO)
O12 = sphere(pos=C1.pos+sph2cart(C_O, deg2rad(109.5), deg2rad(240)), radius=rO, color=color.green, mass=mO)
C2 = sphere(pos=C1.pos+sph2cart(C_C, deg2rad(109.5), deg2rad(120)), radius=rC, color=color.yellow, mass=mC)
H2 = sphere(pos=C2.pos+sph2cart(C_H, deg2rad(180), 0), radius=rH, color=color.blue, mass=mH)
O2 = sphere(pos=C2.pos+sph2cart(C_O, deg2rad(70.5), deg2rad(180)), radius=rO, color=color.green, mass=mO)
H22 = sphere(pos=O2.pos+sph2cart(O_H, 0, 0), radius=rH, color=color.blue, mass=mH)

# take special care of bond angles, this is a very rough (and incomplete) idea of the simulation
# think of an algo to make it infinite
# think of how to incorporate the forces
# thora thora kaam daily cause NO TIMEEE...
