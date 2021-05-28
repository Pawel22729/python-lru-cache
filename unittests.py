#/usr/bin/env python3

import unittest
import time
from helpers import lru

factorialFor = [4,26,836,9172,75234,123456]
ll = lru.LinkedList(len(factorialFor))


class lruTest(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def testColdCache(self):
        for number in factorialFor:
            print("Calculating cold factorial for %s" % number)
            ll.getElement(number)
            self.assertEqual(1, 1)

    def testWarmCache(self):
        for number in factorialFor:
            print("Calculating hot factorial for %s" % number)
            ll.getElement(number)
            self.assertEqual(1, 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(lruTest)
    unittest.TextTestRunner(verbosity=0).run(suite)