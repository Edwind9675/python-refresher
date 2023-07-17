import unittest
import physics

#phy = physics()

class TestPhysics(unittest.TestCase):

    def test_buoyancy_cal(self):
        self.assertEqual(physics.calculate_buoyancy(50, 1000), )

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(50), True)

    def test_pressure_cal(self):
        self.assertEqual(physics.calculate_pressure(100), 1000)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(100, 50), 2)
        self.assertNotEqual(physics.calculate_acceleration(100, 50), 3)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(60,1), 60)
        self.assertNotEqual(physics.calculate_angular_acceleration(60,1), 2)

    def test_calc_torque(self):
        self.assertEqual(physics.calculate_torque(3, 0, 1), 3)
        self.assertNotEqual(physics.calculate_torque(3, 0, 1), 4)

    def test_calc_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(3, 1), 3)
        self.assertNotEqual(physics.calculate_moment_of_inertia(3, 1), 4)

    def test_calc_auv_acceleration(self):
        self.assertEqual(physics.calculate_auv_acceleration(100, 0, 100, .1, 100), [[100], [0]])
        self.assertNotEqual(physics.calculate_auv_acceleration(100, 0, 100, .1, 100), [[100], [1]])

    def test_calc_auv2_acceleration(self):
        self.assertEqual(physics.calculate_auv2_acceleration([[1]
                                                              [1]
                                                              [1]
                                                              [1]], 0, 10, 0), 0)
        self.assertNotEqual(physics.calculate_auv2_acceleration([[1]
                                                              [1]
                                                              [1]
                                                              [1]], 0, 10, 0), 1)

    def test_calc_auv2_angular_acceleration(self):
        self.assertEqual(physics.calculate_auv2_angular_acceleration([[1]
                                                              [1]
                                                              [1]
                                                              [1]], 1, 1, 0, 1), 1)
        self.assertNotEqual(physics.calculate_auv2_angular_acceleration([[1]
                                                              [1]
                                                              [1]
                                                              [1]], 1, 1, 0, 1), 0)          
if __name__ == "__main__":                                                                                                                               
    if __name__ == "__main__":
        unittest.main()