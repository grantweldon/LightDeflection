from __future__ import division
from visual import *
from visual.graph import *

# initialize constants
G=6.67e-11 # Newton's gravitational constant
nm = 1e-9 # define nanometers in terms of meters
h=6.626e-34 # Planck's constant
c=3e8 # speed of light
wavelength=700*nm # initial wavelength

# initialize display
scene = display(center = (0,0,0), background = color.white)

# create black hole
solarmass = 2e30 # solar mass in kg
blackhole_mass = 20*solarmass # define mass of BH
blackhole_radius = 2*G*blackhole_mass/(c**2) # Schwarzschild radius
blackhole_pos=vector(0,0,0)
blackhole = sphere(pos=blackhole_pos, radius = blackhole_radius, color=color.black)

# create photon
initial_pos_photon=vector(c*.0005,c*.01,0)
photon = sphere(pos=initial_pos_photon, radius = 10e-35, color=color.red)
photon.trail = curve(color=photon.color)  

# initialize photon movement
photon_velocity = vector(0,-c,0)

# initialize time and time step
t=0
dt=.0001

# loop
while t<.02:
    rate(30)

    # position vector between photon and BH
    r= photon.pos - blackhole.pos

    # "acceleration" of photon due to gravitational force from BH
    accel_photon_by_bh = ((-G*blackhole_mass)/mag2(r))*norm(r)

    # velocity update
    photon_velocity = photon_velocity + accel_photon_by_bh*dt

    # position update
    photon.pos = photon.pos + photon_velocity*dt

    # wavelength
    wavelength_new=(c*wavelength)/(mag(photon_velocity))

    # update color of photon
    if wavelength_new >701*nm:
        photon.color=color.black

    if wavelength_new >665*nm and wavelength_new<701*nm:
        photon.color=color.red

    if wavelength_new >630*nm and wavelength_new<665*nm:
        photon.color=color.orange

    if wavelength_new >600*nm and wavelength_new<630*nm:
        photon.color=color.yellow

    if wavelength_new >550*nm and wavelength_new<600*nm:
        photon.color=color.green

    if wavelength_new >470*nm and wavelength_new<550*nm:
        photon.color=color.blue

    if wavelength_new <470*nm and wavelength_new>425*nm:
        photon.color=color.blue

    photon.trail.append(pos=photon.pos,color=photon.color)
   
    t=t+dt
