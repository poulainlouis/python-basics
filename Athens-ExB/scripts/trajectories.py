# -*- coding: utf-8 -*-

# trajectories.py -- Python module to study the single-particle movement in 
# electromagnetic fields
# Copyright (C) 2015 IPFN, Instituto Superior Técnico
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

__author__ = 'N. Pinhão <npinhao@ctn.ist.utl.pt>'
__date__ = '16 January 2015'
__version__ = '$Revision: 0.5$'


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.style.use('ggplot')

q = 1; me = 1; Mp = 10*me; B0 = np.array([0,0,1])  # Module of charge, mass and magnetic field

def computeTrajectories(func, E0=np.zeros(3), **keywords):
  """Movement of electron and ion under a constant magnetic field.
  
  Positional arguments:
  func -- the name of the function computing dy/dt at time t0
  Keyword arguments:
  E0 -- Constant component of the electric field
  All other keyword arguments are collected in a 'keywords' dictionary 
  and are specific to each func."""
    
  from scipy.integrate import odeint
    
  # Processes the func specific arguments
  re0, rp0 = "ri" in keywords.keys() and keywords["ri"] or [np.zeros(3),np.zeros(3)]
  if "vi" in keywords.keys():   # Initial velocity
    v0 = keywords["vi"]
  else:
    v0 = np.array([0,1,0])
  wce, wcp = "wc" in keywords.keys() and keywords["wc"] or [0,0]

  tf = 350; NPts = 10*tf; t = np.linspace(0,tf,NPts)  # Time points

  # Integration of the equations of movement
  Q0 = np.concatenate((re0,v0))                  # Initial values
  if "wc" in keywords.keys():
    keywords["wc"] = wce
  Qe = odeint(func, Q0, t, args=(-q/me,E0,B0,keywords))  # Trajectory for the "electron"
  Q0 = np.concatenate((rp0,v0))                  # Initial values
  if "wc" in keywords.keys():
    keywords["wc"] = wcp
  Qp = odeint(func, Q0, t, args=(q/Mp,E0,B0,keywords))   # Trajectory for the "ion"
  
  return Qe, Qp

def plotGradB(re,rp,gradx,grady):
  r0 = np.zeros(3)
  fig = plt.figure(figsize=(8,7))
  plt.plot(re[:,0],re[:,1], rp[:,0],rp[:,1], r0[0],r0[1],'o',
           re[-1,0],re[-1,1],'>',rp[-1,0],rp[-1,1],'<')
  plt.title("Trajectories for dB/dx and dB/dy gradients",fontsize="x-large")
  plt.xlabel("x-x$_{gc}$",fontsize="large"); plt.ylabel("y-y$_{gc}$",fontsize="large")
  #plt.ylim(ymax=15)
  plt.suptitle("$dB_z/dx = %3.1f,\,dB_z/dy = %3.1f$" % (gradx,grady), fontsize=16)
  dummy = plt.legend(["e","p"])
  
def plotMirror(re0,rp0,re,rp,zMax):
  from mpl_toolkits.mplot3d import Axes3D
  
  # Plot the trajectories and Larmor radius
  fig = plt.figure(figsize=(8,6))
  fig.clf()
  ax = fig.gca(projection='3d')
  ax.scatter(re0[0],re0[1],re0[2],c='red')      # Starting point
  ax.scatter(rp0[0],rp0[1],rp0[2],c='red')      # Starting point
  # Legibility
  ax.set_title("Trajectories",fontsize=18)
  ax.set_xlabel("X Axis",fontsize=16); ax.set_ylabel("Y Axis",fontsize=16)
  ax.set_zlabel("Z Axis",fontsize=16)
  #ax.text(17,15,200, "$\\uparrow\\, \\vec{B}$", color="red",fontsize=20)
  Qe = re[np.where(re[:,2]<1.02*zMax)]
  ax.plot(Qe[:,0],Qe[:,1],Qe[:,2])              # Electron trajectory
  # Final points
  ax.scatter(Qe[-1,0],Qe[-1,1],Qe[-1,2],c='green', marker='>')

  Qp = rp[np.where(rp[:,2]<1.02*zMax)]
  ax.plot(Qp[:,0],Qp[:,1],Qp[:,2])              # Electron trajectory
  # Final points
  ax.scatter(Qp[-1,0],Qp[-1,1],Qp[-1,2],c='yellow', marker='>')
  
def plotPolariz(Qe,Qp):
    r0 = np.zeros(3)
    fig = plt.figure(figsize=(8,6))
    plt.plot(Qe[:,0],Qe[:,1], Qp[:,0],Qp[:,1])
    plt.plot(r0[0],r0[1],'ro')
    plt.plot(Qe[-1,0],Qe[-1,1],'>',Qp[-1,0],Qp[-1,1],'<')
    plt.title("Trajectories for a polarization E field",fontsize="x-large")
    plt.xlabel("x",fontsize="large"); plt.ylabel("y-y$_{gc}$",fontsize="large")
    plt.grid()
    dummy = plt.legend(["e","p"])

