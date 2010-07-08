#!/usr/bin/env python
'''
Created on Apr 3, 2010

@author: brianjinwright
'''
import unittest
from cloudstory import get_driver
from test_settings import *

class NirvanixAuthTestCase(unittest.TestCase):
    """Nirvanix Auth Test Case"""

    def setUp(self):
        c_driver = get_driver('nirvanix')
        self.nvx = c_driver(    
            NIRVANIX_USERNAME,
            NIRVANIX_PASSWORD,
            NIRVANIX_APPKEY
            )
        
    def testLogin(self):
        self.failIf(
            getattr(
                self.nvx,
                'session_key',
                None
                ) == None,
            'Session Key must be available'
            )
#
    def testLogout(self):
        cs = self.nvx.logout()
        self.assertEquals(cs.content.ResponseCode._,'0')
        
    

if __name__ == "__main__":
    
    unittest.main()