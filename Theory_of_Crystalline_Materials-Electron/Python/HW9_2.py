# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:16:37 2018

@author: Kman
"""

import numpy as np
import math

A=np.mat("3 -1;-1 3")
B=np.mat("0 0 ;-1 0")
C=np.mat("0 -1 ;0 0")
D=np.mat("0 0 ;-1 0")
E=np.mat("0 -1 ;0 0")

A2=np.mat("6 0 ;0 6")
B2=np.mat("-1 0 ;0 -1")
C2=np.mat("-1 0 ;0 -1")
D2=np.mat("-1 0 ;0 -1")
E2=np.mat("-1 0 ;0 -1")
F2=np.mat("-1 0 ;0 -1")
G2=np.mat("-1 0 ;0 -1")
#F=1-1 G-11

A3=np.mat("3 0 ;0 3")
F3=np.mat("0 -1 ;-1 0")
G3=np.mat("0 -1 ;-1 0")
H3=np.mat("0 -1 ;0 0")
#-1-1
I3=np.mat("0 0;-1 0")
#11

A4=np.mat("6 0 ;0 6")
B4=np.mat("0 -1 ;0 0")
C4=np.mat("0 0 ;-1 0")
D4=np.mat("0 -1 ;0 0")
E4=np.mat("0 0 ;-1 0")
J4=np.mat("0 0 ;-1 0")
#02 or 20
K4=np.mat("0 -1 ;0 0")
#-20 0-2
L4=np.mat("0 -1;0 0")
#1-2 -21
M4=np.mat("0 0 ;-1 0")
#-12 2-1
i=0
ka=0
kb=0

while ka<=0.5:
    kb=ka
    kB = complex(math.cos(ka*2*math.pi),math.sin(ka*2*math.pi))
    kC = complex(math.cos(-ka*2*math.pi),math.sin(-ka*2*math.pi))
    kD = complex(math.cos(kb*2*math.pi),math.sin(kb*2*math.pi))
    kE = complex(math.cos(-kb*2*math.pi),math.sin(-kb*2*math.pi))
    kF = complex(math.cos((ka-kb)*2*math.pi),math.sin((ka-kb)*2*math.pi))
    kG = complex(math.cos((-ka+kb)*2*math.pi),math.sin((-ka+kb)*2*math.pi))
    kH = complex(math.cos((-ka-kb)*2*math.pi),math.sin((-ka-kb)*2*math.pi))
    kI = complex(math.cos((ka+kb)*2*math.pi),math.sin((ka+kb)*2*math.pi))
    kJ = complex(math.cos(2*ka*2*math.pi),math.sin(2*ka*2*math.pi))+complex(math.cos(2*kb*2*math.pi),math.sin(2*kb*2*math.pi))
    kK = complex(math.cos(-2*kb*2*math.pi),math.sin(-2*kb*2*math.pi)) + complex(math.cos(-2*ka*2*math.pi),math.sin(-2*ka*2*math.pi))    
    kL = complex(math.cos((-2*ka+kb)*2*math.pi),math.sin((-2*ka+kb)*2*math.pi)) + complex(math.cos((-2*kb+ka)*2*math.pi),math.sin((-2*kb+ka)*2*math.pi))
    kM = complex(math.cos((-ka+2*kb)*2*math.pi),math.sin((-ka+2*kb)*2*math.pi)) + complex(math.cos((-kb+2*ka)*2*math.pi),math.sin((-kb+2*ka)*2*math.pi))
    Dk = -6.3182*(A + B*kB + C*kC + D*kD + E*kE) + 0.5063*(A2 + B2*kB + C2*kC + D2*kD + E2*kE + F2*kF + G2*kG) - 0.416*(A3 + F3*kF + G3*kG + H3*kH + I3*kI) + 0.3543*(A4 + B4*kB + C4*kC + D4*kD + E4*kE + J4*kJ + K4*kK + L4*kL + M4*kM)   
    An = np.linalg.eigvals(Dk)
    s=An[i]
    x=np.sign(s)*np.sqrt(abs(s)/(12.011*1.66054*10**-27*6.2415*10**-2))*6.582*10**-16*8065.6
    y=abs(x)
    print(y)

    ka=ka+0.01
ka=0.5
kb=0.5

while ka<=2/3:
    kb=-ka+1
    kB = complex(math.cos(ka*2*math.pi),math.sin(ka*2*math.pi))
    kC = complex(math.cos(-ka*2*math.pi),math.sin(-ka*2*math.pi))
    kD = complex(math.cos(kb*2*math.pi),math.sin(kb*2*math.pi))
    kE = complex(math.cos(-kb*2*math.pi),math.sin(-kb*2*math.pi))
    kF = complex(math.cos((ka-kb)*2*math.pi),math.sin((ka-kb)*2*math.pi))
    kG = complex(math.cos((-ka+kb)*2*math.pi),math.sin((-ka+kb)*2*math.pi))
    kH = complex(math.cos((-ka-kb)*2*math.pi),math.sin((-ka-kb)*2*math.pi))
    kI = complex(math.cos((ka+kb)*2*math.pi),math.sin((ka+kb)*2*math.pi))
    kJ = complex(math.cos(2*ka*2*math.pi),math.sin(2*ka*2*math.pi))+complex(math.cos(2*kb*2*math.pi),math.sin(2*kb*2*math.pi))
    kK = complex(math.cos(-2*kb*2*math.pi),math.sin(-2*kb*2*math.pi)) + complex(math.cos(-2*ka*2*math.pi),math.sin(-2*ka*2*math.pi))    
    kL = complex(math.cos((-2*ka+kb)*2*math.pi),math.sin((-2*ka+kb)*2*math.pi)) + complex(math.cos((-2*kb+ka)*2*math.pi),math.sin((-2*kb+ka)*2*math.pi))
    kM = complex(math.cos((-ka+2*kb)*2*math.pi),math.sin((-ka+2*kb)*2*math.pi)) + complex(math.cos((-kb+2*ka)*2*math.pi),math.sin((-kb+2*ka)*2*math.pi))
    Dk = -6.3182*(A + B*kB + C*kC + D*kD + E*kE) + 0.5063*(A2 + B2*kB + C2*kC + D2*kD + E2*kE + F2*kF + G2*kG) - 0.416*(A3 + F3*kF + G3*kG + H3*kH + I3*kI) + 0.3543*(A4 + B4*kB + C4*kC + D4*kD + E4*kE + J4*kJ + K4*kK + L4*kL + M4*kM)   
    An = np.linalg.eigvals(Dk)
    s=An[i]
    x=np.sign(s)*np.sqrt(abs(s)/(12.011*1.66054*10**-27*6.2415*10**-2))*6.582*10**-16*8065.6
    y=abs(x)
    print(y)

    ka=ka+0.01

ka=2/3
kb=1/3
while ka>=0:
    kb=ka/2
    kB = complex(math.cos(ka*2*math.pi),math.sin(ka*2*math.pi))
    kC = complex(math.cos(-ka*2*math.pi),math.sin(-ka*2*math.pi))
    kD = complex(math.cos(kb*2*math.pi),math.sin(kb*2*math.pi))
    kE = complex(math.cos(-kb*2*math.pi),math.sin(-kb*2*math.pi))
    kF = complex(math.cos((ka-kb)*2*math.pi),math.sin((ka-kb)*2*math.pi))
    kG = complex(math.cos((-ka+kb)*2*math.pi),math.sin((-ka+kb)*2*math.pi))
    kH = complex(math.cos((-ka-kb)*2*math.pi),math.sin((-ka-kb)*2*math.pi))
    kI = complex(math.cos((ka+kb)*2*math.pi),math.sin((ka+kb)*2*math.pi))
    kJ = complex(math.cos(2*ka*2*math.pi),math.sin(2*ka*2*math.pi))+complex(math.cos(2*kb*2*math.pi),math.sin(2*kb*2*math.pi))
    kK = complex(math.cos(-2*kb*2*math.pi),math.sin(-2*kb*2*math.pi)) + complex(math.cos(-2*ka*2*math.pi),math.sin(-2*ka*2*math.pi))    
    kL = complex(math.cos((-2*ka+kb)*2*math.pi),math.sin((-2*ka+kb)*2*math.pi)) + complex(math.cos((-2*kb+ka)*2*math.pi),math.sin((-2*kb+ka)*2*math.pi))
    kM = complex(math.cos((-ka+2*kb)*2*math.pi),math.sin((-ka+2*kb)*2*math.pi)) + complex(math.cos((-kb+2*ka)*2*math.pi),math.sin((-kb+2*ka)*2*math.pi))
    Dk = -6.3182*(A + B*kB + C*kC + D*kD + E*kE) + 0.5063*(A2 + B2*kB + C2*kC + D2*kD + E2*kE + F2*kF + G2*kG) - 0.416*(A3 + F3*kF + G3*kG + H3*kH + I3*kI) + 0.3543*(A4 + B4*kB + C4*kC + D4*kD + E4*kE + J4*kJ + K4*kK + L4*kL + M4*kM)   
    An = np.linalg.eigvals(Dk)
    s=An[i]
    x=np.sign(s)*np.sqrt(abs(s)/(12.011*1.66054*10**-27*6.2415*10**-2))*6.582*10**-16*8065.6
    y=abs(x)
    print(y)
    ka=ka-0.005
