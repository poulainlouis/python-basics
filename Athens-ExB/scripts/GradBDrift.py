#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

global q,m


def BField(x):
  """Campo magnético"""
  B0 = 1
  return B0*(1+0.566*x[1])


def Motion(Q,t):
  """ Equações do movimento
  
  Nota: Com os valores usados, rL / (grad(B)/B) == coeficiente de Q[1] que tem de ser << 1 para a aproximação ser válida.
  """
  global q,m
  
  q_m = q/m
  #B = BField(Q[:2]) # (x,y)
  B = 1*(1+0.266*Q[1])
  v = Q[2:]
  
  dq = v
  dv = q_m*np.array([v[1],-v[0]])*B
  
  return dq[0], dq[1], dv[0], dv[1]


def main():
  
  global q,m

  m = 1; q = 1

  r0 = np.zeros(2)
  v0 = np.array([0,1])
  rL = m/q*np.sqrt(np.dot(v0,v0))/BField(r0)
  Q0 = np.concatenate((r0,v0))
  
  tf = 30
  NPts = 1000;
  tspan = np.linspace(0,tf,NPts)
  
  Q = odeint(Motion, Q0, tspan, rtol=1e-12, atol=1e-14)
  
  #plt.figure()
  plt.plot(Q[:,0],Q[:,1], r0[0],r0[1],'o',Q[-1,0],Q[-1,1],'<')
  #plt.savefig('B1.png')
  plt.show()


if __name__ == "__main__":
  main()
