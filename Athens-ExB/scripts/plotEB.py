import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot3d(Re, Ri, Rd, t, rLe, rLp, We, Wp, angle):
    """Plot the trajectories of the electron, the ion and the drift trajectory"""   
    fig = plt.figure(figsize=(13,10))
    
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    # Starting point
    r0 = np.zeros(3); ax.scatter(r0[0],r0[1],r0[2],c='red')
    # Electron and ion trajectories
    ax.plot(Re[:,0],Re[:,1],Re[:,2]); ax.scatter(Re[-1,0],Re[-1,1],Re[-1,2],c='green', marker='>')
    #ax.contour(Re[:,0],Re[:,1],Re[:,2], zdir='z', offset=-50, cmap=cm.coolwarm)
    #ax.contour(Re[:,0],Re[:,1],Re[:,2], zdir='y', offset=200, cmap=cm.coolwarm)
    ax.plot(Ri[:,0],Ri[:,1],Ri[:,2]); ax.scatter(Ri[-1,0],Ri[-1,1],Ri[-1,2],c='yellow', marker='>')
    # Drift trajectory
    ax.plot(Rd[:,1],Rd[:,2],zdir='z',linestyle='--')
    
    ax.set_title("Trajectories", fontsize=16)
    ax.set_xlabel("X Axis", fontsize=14); ax.set_ylabel("Y Axis", fontsize=14); ax.set_zlabel("Z Axis", fontsize=14)
    if angle < 270:
      xpos = np.min(Re[:,0])
    else:
      xpos = np.max(Re[:,0])
    zpos = np.min(Re[:,2]) + 3/4*(np.max(Re[:,2])-np.min(Re[:,2]))
    ax.text(xpos,0,zpos, "$\\uparrow\\,\\vec{B}$", color="red", fontsize=20)
    ax.view_init(30,angle)
    #ax.set_zlim3d(-5e3, 5e3)
    #ax.set_axis_off()
    
    ax = fig.add_subplot(2, 2, 2)
    #print(len(t),len(rLe),len(rLp))
    plt.plot(t,rLe,t,rLp)
    plt.title("Larmor radius", fontsize=16)
    plt.xlabel("t", fontsize=14); plt.ylabel("r$_L\\times (qB/v_\perp)$", fontsize=14)
    plt.legend(["e","p"], fontsize=14)

    v2e = (Re[:,3]**2+Re[:,4]**2+Re[:,5]**2)/2
    v2p = 10*(Ri[:,3]**2+Ri[:,4]**2+Ri[:,5]**2)/2
 
    ax = fig.add_subplot(2, 2, 3)
    plt.plot(t,We,t,Wp)
    plt.title("Kinetic energy", fontsize=16)
    plt.xlabel("t", fontsize=14); plt.ylabel("W", fontsize=14)
    plt.legend(["e","p"], loc=2, fontsize=14)
    #plt.show()
