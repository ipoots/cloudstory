#!/usr/bin/env python
'''
Created on Apr 3, 2010

@author: brianjinwright
'''
import unittest
from test_settings import \
NIRVANIX_USERNAME, NIRVANIX_PASSWORD,\
NIRVANIX_APPKEY

from cloudstory.nirvanix import Nirvanix


class NirvanixAuthTestCase(unittest.TestCase):
    """Nirvanix Auth Test Case"""

    def setUp(self):
        self.nvx = Nirvanix(
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