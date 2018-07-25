import numpy as np
import matplotlib.pyplot as plt

t = 0                                   #initial time
N = 100                                 #duration of simulation
dt = 0.1                                #timestep of integration
m = 2                                   #mass of a single Argon atom
#k = float(input("Spring constant for molecule:"))
#x0 = float(input("Equilibrium length of the spring:"))
#x1 = float(input("Initial position for Particle 1:"))
#v1 = float(input("Initial velocity for Particle 1:"))
#x2 = float(input("Initial position for Particle 2:"))
#v2 = float(input("Initial velocity for Particle 2:"))
k = 0.2
x0 = 1
x1 = 0
v1 = 0
x2 = 1
v2 = 1

F0 = k*(x2-x1-x0)                        #Force of two particles connected by a spring

while t <= N:
    x1 = x1 + dt*v1 + ((dt**2)*0.5*(F0/m))         #positons at current time
    x2 = x2 + dt*v2 - ((dt**2)*0.5*(F0/m))
    F = k*(x2-x1-x0)                              #calculate new forces
    v1 = v1 + 0.5*dt*(F0+F)/m                   #calculate new velocities
    v2 = v2 - 0.5*dt*(F0+F)/m
    plt.plot(t, (x2-x1), "bo")                                # Plot function
    t = t + dt

plt.title('Molecular Dynamics of an Argon molecule')
plt.xlabel('t')
plt.ylabel('x')
plt.show()
