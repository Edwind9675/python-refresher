import numpy as np

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
       torque = r*F_magnitude* np.cos(F_direction) + r*F_magnitude* np.sin(F_direction)
       return torque

def calculate_moment_of_inertia(m, r):
       """calculates the moment of inertia of an object given 
       its mass and the distance from the axis of rotation to 
       the center of mass of the object."""
       mi = m*r*r
       return mi

def calculate_auv_acceleration(F_magitude, F_angle, mass, volume, thruster_distance):
       """calculates the acceleration of the AUV in the 2D plane."""
       mass = 100 #kg
       volume = 0.1 #m^3
       accx = F_magitude*np.cos(F_angle) / mass
       accy = F_magitude*np.sin(F_angle) / mass
       acc_total = accx + accy 
       return acc_total

def calculate_auv_angular_acceleration(F_magnitude, F_angle, intertia, thruster_disance):
       """calculates the angular acceleration of the AUV."""
       angular_acc = calculate_torque.torque()*thruster_disance / intertia 
       return angular_acc

def calculate_auv2_acceleration(np.ndarray(T))