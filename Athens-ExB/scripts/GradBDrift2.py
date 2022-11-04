#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

global E0,B0


def Motion(Q,t,qbym):
  """ Equações do movimento"""
  global E0,B0
  
  v = Q[3:]
  dv = qbym*(E0 + np.cross(v,B0))
  
  return v[0], v[1], v[2], dv[0], dv[1], dv[2]


def main():
  
  global E0,B0

  me = 1; Mi = 10; q = 1 

  r0 = np.zeros(3)
  v0 = np.array([0,1,0])
  E0 = np.array([1,1,0])
  B0 = np.array([0,0,1])
  
  #rL = q*np.sqrt(v0[0]^2+v0[1]^2)/(m*BField(x0))
  
  Q0 = np.concatenate((r0,v0))

  tf = 125
  NPts = 30*tf
  tspan = np.linspace(0,tf,NPts)
  
  #Motion(Q0,tspan[0])
  qbym = -q/me
  Qe = odeint(Motion, Q0, tspan, args=(qbym,), rtol=1e-12, atol=1e-14)
  qbym = q/Mi
  Qi = odeint(Motion, Q0, tspan, args=(qbym,), rtol=1e-12, atol=1e-14)
  
  fig = plt.figure()
  ax = fig.gca(projection='3d')
  ax.plot(Qe[:,0],Qe[:,1],Qe[:,2])
  ax.plot(Qi[:,0],Qi[:,1],Qi[:,2])
  ax.scatter(r0[0],r0[1],r0[2],c='red')
  ax.scatter(Qe[-1,0],Qe[-1,1],Qe[-1,2],c='green')
  ax.scatter(Qi[-1,0],Qi[-1,1],Qi[-1,2],c='yellow')
  ax.set_xlabel("X Axis")
  ax.set_ylabel("Y Axis")
  ax.set_zlabel("Z Axis")
  #plt.savefig('B1.png')
  plt.show()


if __name__ == "__main__":
  main()
