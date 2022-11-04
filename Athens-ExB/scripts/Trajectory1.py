import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""Movement of electron and ion under a constant magnetic field"""

def EqMovement(Q,t,qbym):
    """Equations of movement"""
    global B0
    v = Q[3:]
    drdt = v                                    # Velocity
    dvdt = qbym*np.cross(v,B0)                  # Acceleration
    return np.concatenate((drdt,dvdt))
  
def trajectories(Q0, QbyM, tf):
  """Computes the electron and proton trajectories"""
  
  NPts = 5*tf; t = np.linspace(0,tf,NPts)

  # Integration of the equations of movement
  Qe = odeint(EqMovement, Q0, t, args=(QbyM[0],))
  Qp = odeint(EqMovement, Q0, t, args=(QbyM[1],))
  return Qe, Qp

def initFigure():
  line1.set_data([], []); line1b.set_data([], [])
  line2.set_data([], []); line2b.set_data([], [])
  # Legibility
  ax.set_title("Trajectories",fontsize=18)
  ax.set_xlabel("X Axis",fontsize=16); ax.set_ylabel("Y Axis",fontsize=16)
  return line1, line1b, line2, line2b

def animate(i,re, rp):
  line1b.set_data(re[:i,0],re[:i,1]); line1.set_data(re[i,0],re[i,1])
  line2b.set_data(rp[:i,0],rp[:i,1]); line2.set_data(rp[i,0],rp[i,1])
  return line1, line1b, line2, line2b

  
global B0

# Constants
q = 1; me = 0.3; Mp = 30*me; Bz = 2
# Initial conditions
v0z = 0
r0 = np.zeros(3); v0 = np.array([2,0,v0z])  # Initial position and velocity
B0 = np.array([0,0,Bz])                     # Magnetic fields

# Frequency and radius
we = q*B0[2]/me; wp = q*B0[2]/Mp            # Cyclotron frequencies    
modv = np.sqrt(v0[0]**2+v0[1]**2)           # Perpendicular|B velocity
rLe = me/q*modv/Bz; rLp = Mp/me*rLe         # Larmor radius

print('Cyclotron frequencies      Larmor radius\n   we= {0}, wp= {1}  \
rLe= {2}, rLp= {3}'.format(we,wp,rLe,rLp))

tf = 160
# Computes the trajectories
QbyM = np.array([-q/me,q/Mp])               # Charge by mass ratio
Q0 = np.concatenate((r0,v0))                # Initial values
Qe,Qp = trajectories(Q0, QbyM, tf)          # Integrate the equations of movement

# Plots the trajectories
plt.style.use('ggplot')
fig = plt.figure(figsize=(9,8))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-15,15), ylim=(-25,5))

line2, = ax.plot([], [], 'ro', markersize=12); line2b, = ax.plot([], [], 'r--')
line1, = ax.plot([], [], 'bo'); line1b, = ax.plot([], [], 'b--')

ani = animation.FuncAnimation(fig, animate, np.linspace(0,tf,5*tf), fargs=(Qe,Qp),
                              blit=False, interval=1,
                              repeat = False, init_func=initFigure)
#ani.save('uniformB.mp4', fps=15)
plt.show()
    
