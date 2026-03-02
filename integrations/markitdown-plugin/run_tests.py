import sys
import unittest
import pprint
import xmlrunner

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromName('tests')
    testResult = xmlrunner.XMLTestRunner(output='test-reports').run(tests)
    sys.exit(not testResult.wasSuccessful())
