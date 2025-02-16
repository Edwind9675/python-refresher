import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.81 #m/s^2


def calculate_buoyancy( v, density_fluid): 
        
        
        #self.density_fluid = 1000 
        """using the formula buoyancy = density of fluid mult by object volume and gravitational constant, 
        we will yield the density by applying that the density of water is 1000 kg/m^3, 
        and gravitation constant is 9.81, and any volume specified. """
        fb = g * v * density_fluid
        return fb

def will_it_float(mass):
        
        fg = mass * g 
        """ sicne ofrce of gravity is also present in the water, we can compare the force of buoyancy(up) 
        and force of gravity(down), and knowing if the previous num is larger, the object will float, and otherwise."""
        if fg < calculate_buoyancy.fb :
            return (True)
        else: 
            return (False)
        
def calculate_pressure(depth):
       
        density_water = 1000 #kg/m^3
        """the formula of presusre is equal to density of water
        multiply by the depth and gravitational force """
        #depth is denoted as depth in m 
        p = density_water*depth*g
        return p + "pascal" + 1
    

"""a = physics()
print(a.calculate_buoyancy(50, 1000))
print(a.will_it_float(50))
print (a.calculate_pressure(100))"""

def calculate_acceleration(F, m): 
     
        a = F/m   #since f = ma, by dividing m from both sides, we yield acceleration
        """in this question, we calculate the acceleation of an object given the force appllied 
        to it and its mass, where F is he force applied in N and m is the mass in kg"""
        return a

def calculate_angular_acceleration(tau, I): 
      """calculates the torque applied to an object given the force 
      applied to it and the distance from the axis of rotation to the point where the force is applied."""
      aac = tau/I  
      return aac 

def calculate_torque(F_magnitude, F_direction, r):
     
       """calculates the torque applied to an object given the force applied to it and 
       the distance from the axis of rotation to the point where the force is applied."""
       F_dir = np.deg2rad(F_direction)
       torque = r*F_magnitude* np.cos(F_dir) + r*F_magnitude* np.sin(F_dir)
       return torque

def calculate_moment_of_inertia(m, r):
       """calculates the moment of inertia of an object given 
       its mass and the distance from the axis of rotation to 
       the center of mass of the object."""
       mi = m*r*r
       return mi

def calculate_auv_acceleration(F_magitude, F_angle, mass) :
       """calculates the acceleration of the AUV in the 2D plane."""
       #mass = 100 #kg
       #volume = 0.1 #m^3
       accx = F_magitude*np.cos(F_angle)/ mass
       accy = F_magitude*np.sin(F_angle)/ mass
       acc_total = accx + accy 
       return np.array([[accx, accy]]) #

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia, thruster_distance):
       """calculates the angular acceleration of the AUV."""
       angular_acc = calculate_torque.torque(F_magnitude, F_angle, thruster_distance)*thruster_distance / inertia
       return angular_acc


def calculate_auv2_acceleration(T, alpha, mass, theta):
       """"Calculate the acceleration of an AUV given it has 4 thrusters"""
       """alpha is the system angle in degree, T is a 4x1 matrix, and mass in kg, theta is the global angle in degree"""
       if T.shape == (4, 1):
              component_matrix= np.array(
                    [ [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                     [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)] ]
              ) 
              rotation_matrix= np.array(
                    [ [np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)] ]
              ) 
              fxyprime = np.matmul(component_matrix, T) 
              
              acceleration_fxy = (np.matmul(fxyprime, rotation_matrix))/mass
              
              acceleration_mag = math.sqrt(sum(pow(element, 2) for element in acceleration_fxy))
              return acceleration_fxy
       else: 
              raise TypeError("dimension invalid")

def calculate_auv2_angular_acceleration(T, L, l, alpha, inertia):
       """Calculate the angular acceleration of a 4 thruster AUV, aka the torque acceleration"""
       component_matrix= np.array(
                    [ [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                     [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)] ]
              ) 
       force_fxy = np.matmul(component_matrix, T)
       accl = np.array([force_fxy[0] / inertia, force_fxy[1] / inertia])
       r = np.sqrt(L*L +l*l)
       mag = np.sqrt(force_fxy[0]**2 + force_fxy[1]**2)
       return calculate_torque(mag, alpha, r)

def simulation_auv2_motion(T, alpha, L, l, inertia=100, dt=.1, t_final=10, x0=0, y0=0, theta0=0):
       #time_step = 0.01
       # dt is essentially timestep
       state = np.ndarray([x0], [y0], [theta0])
       time = np.arange(0, t_final, dt)
       x = np.zeros_like(time)
       y = np.zeros_like(time)
       x[0]= x0
       y[0]=y0
       position = np.zeros_like(time)
       velocity = np.zeros_like(time) 
       angular_displacement = np.zeros_like(time)
       angular_acceleration = np.zeros_like(time)
       theta = np.zeros_like(time)
       theta[0] = theta0
       mass = 100 #kg
       omega= np.zeros_like(time) 
       a = np.tile(np.zeros_like(time), (2, 1))
       a[0] = calculate_auv2_acceleration(T, alpha, mass, theta)[0][0]
       omega[0] = calculate_auv2_angular_acceleration(T, L, l, alpha, inertia)[0][0]


      
       for i in range(1, len(time)):
              angular_acceleration[i] = calculate_auv2_angular_acceleration(T, L, l, alpha, inertia)
              a[0][i] = calculate_auv2_acceleration(T, alpha, mass, theta)[0][0]
              a[1][i] = calculate_auv2_acceleration(T, alpha, mass, theta)[0][1]
              velocity[i] = a[i-1]*dt + velocity[i-1]
              x[i] = velocity[i-1]*dt + x[i-1]
              y[i] = velocity[i-1]*dt + y[i-1]
              theta[i] = .5 * a[i]* dt**2 + velocity[i-1]*time[i-1]
              omega[i] = angular_acceleration[i-1]* dt + omega [i-1]
              time[i]= time[i] + time[i-1] 
             
       physicsdict = {
              "acceleration": a,
              "velocity": velocity, 
              "x": x,
              "y": y,
              "theta": theta,
              "omega": omega, 
              "time": time
       }
       return physicsdict

def plot(a, velocity, x, y, theta, omega, time):
       plt.plot(time, a, label="Acceleration(m/s^2)")
       plt.plot(time, velocity, label="Velocity(m/s)")
       plt.plot(time, theta, label="Direction(rad)")
       plt.plot(x, y, label = "position")
       plt.xlabel("Time (s)")
       plt.ylabel("theta(rad), Velocity (m/s), Acceleration (m/s^2)")
       plt.legend()
       plt.show()