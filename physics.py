import numpy as np
import math
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

def calculate_auv_acceleration(F_magitude, F_angle, mass, volume, thruster_distance=100):
       """calculates the acceleration of the AUV in the 2D plane."""
       #mass = 100 #kg
       #volume = 0.1 #m^3
       accx = F_magitude*np.cos(F_angle)*thruster_distance / mass
       accy = F_magitude*np.sin(F_angle)*thruster_distance / mass
       acc_total = accx + accy 
       return np.array([[accx], [accy]]),

def calculate_auv_angular_acceleration(F_magnitude, F_angle, intertia, thruster_distance):
       """calculates the angular acceleration of the AUV."""
       angular_acc = calculate_torque.torque(F_magnitude, F_angle, thruster_distance)*thruster_distance / intertia 
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
              
              acceleration_fxy = np.matmul(fxyprime, rotation_matrix)/mass
              
              acceleration_mag = math.sqrt(sum(pow(element, 2) for element in acceleration_fxy))
              return acceleration_fxy

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