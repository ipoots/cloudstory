#!/usr/bin/env python
'''
Created on Jun 28, 2010

@author: brianjinwright
'''
import unittest
from cloudstory import get_driver
from test_settings import \
CLOUDFILES_AUTH_KEY,CLOUDFILES_AUTH_USER


class CloudFilesAuthTestCase(unittest.TestCase):
    """Nirvanix Auth Test Case"""

    def setUp(self):
        c_driver = get_driver('cloudfiles')
        self.cf = c_driver(
            CLOUDFILES_AUTH_USER,
            CLOUDFILES_AUTH_KEY
            )
        
    def testLogin(self):
        tt = self.cf.login()
        
        self.failIf(
            getattr(
                self.cf,
                'auth_key',
                None
                ) == None,
            'Auth Key must be available'
            )
     
    

if __name__ == "__main__":
    
    unittest.main()