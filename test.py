#!/usr/bin/env python

import sys
import unittest

class TestBareBones(unittest.TestCase):
    def test_one_equals_one(self):
        self.assertEquals(1,1,"1!=1")
        
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('testtest', 'test_bare_bones', TestBareBones)
