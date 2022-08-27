# Python scrpit calculating Pyramidal Horn Antenna parameters
# Written by Michael Altshuler: ALTMIC003

#imports
import math

# Define known paramters:
Gdb = 14
Glinear = 10**(Gdb/10)
freq = 8.25 * 10**9
c = 3 * 10**8
wavelength = c/freq

# Dimensions
a = 0.02286
b = 0.01016

epsilon_ap = 0.458

# Iteration for A
A = epsilon_ap*wavelength*math.sqrt(Glinear)

B = 1/(4*math.pi)*(Glinear*wavelength**2)/(0.5*A)
R1 = A**2/(3*wavelength)
RH = (R1*(A-a))/A
lH = math.sqrt(R1**2+(A/2)**2)
R2 = B**2/(2*wavelength)
RE = (R2*(B-b))/B
lE = R2**2+B**2/4

print("RE = " + str(RE))
print("RH = " + str(RH))
