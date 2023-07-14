import unittest
import physics

#phy = physics()

class TestPhysics(unittest.TestCase):

    def test_buoyancy_cal(self):
        self.assertEqual(physics.calculate_buoyancy(50, 1000), 1000)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(50), True)

    def test_pressure_cal(self):
        self.assertEqual(physics.calculate_pressure(100), 1000)

    #def test_

if __name__ == "__main__":
    unittest.main()