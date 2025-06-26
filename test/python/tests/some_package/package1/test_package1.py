import unittest
from some_package.package1.package1 import p

class TestPackage1(unittest.TestCase):
    def test1(self):
        print(p)
        pass