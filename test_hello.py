import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(4,2), 6)
        self.assertNotEqual(hello.add(4,2), 4)


    def test_sub(self):
        self.assertEqual(hello.sub(4,2), 2)
        self.assertNotEqual(hello.sub(4,2), 4)


    def test_div(self):
        self.assertEqual(hello.div(4,2), 2)
        self.assertNotEqual(hello.div(4,0), ValueError)
    try:
        hello.div(4,0)
    except:
        print ("Can't divide by zero!")

    def test_add(self):
        self.assertEqual(hello.add(4,2), 6)
        self.assertNotEqual(hello.add(4,2), 4)

    # def test_sin(self):
    #     self.assertEqual(hello.sin(0), 0)
    #     self.assertEqual(hello.sin(1), 0.8414709848078965)

    # def test_cos(self):
    #     self.assertEqual(hello.cos(0), 1)
    #     self.assertEqual(hello.cos(1), 0.5403023058681398)

    # def test_tan(self):
    #     self.assertEqual(hello.tan(0), 0)
    #     self.assertEqual(hello.tan(1), 1.5574077246549023)

    # def test_cot(self):
    #     self.assertEqual(hello.cot(0), float("inf"))
    #     self.assertEqual(hello.cot(1), 0.6420926159343306)

    def test_accsummary(self):
        self.assertEqual(hello.accsummary("Eddie", 100, 12345678))

    def test_accprtbal(self):
        self.assertEqual(hello.accprtbal("Eddie", 100, 12345678))

    def test_accwithdraw(self):
        self.assertEqual(hello.accwithdraw(100, 10, 90))

    def test_accdeposit(self): 
        self.assertEqual(hello.accdeposit(100, 10, 110))

if __name__ == "__main__":
    unittest.main()
