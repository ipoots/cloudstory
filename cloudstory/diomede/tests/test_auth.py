#!/usr/bin/env python
'''
Created on Jun 28, 2010

@author: brianjinwright
'''
import unittest
from cloudstory import get_driver
from test_settings import *


class DiomedeAuthTestCase(unittest.TestCase):
    """Nirvanix Auth Test Case"""

    def setUp(self):
        diomede = get_driver('diomede')
        self.di = diomede(DIOMEDE_USERNAME,DIOMEDE_PASSWORD)
        
#    def testLogin(self):
#        tt = self.di.login()
#        
#        self.failIf(
#            getattr(
#                self.di,
#                'session_token',
#                None
#                ) == None,
#            'Session Token must be available'
#            )
    def testCreateUser(self):
        action = self.di('create_user',
            username=DIOMEDE_NEW_USERNAME,
            password=DIOMEDE_NEW_PASSWORD,
            email=DIOMEDE_NEW_EMAIL)

    
#    def testDeleteUser(self):
#        diomede = get_driver('diomede')
#        self.di = diomede(DIOMEDE_NEW_USERNAME,DIOMEDE_NEW_PASSWORD)
#        action = self.di('delete_user',
#                session_token=self.di.session_token)
#        print 'delete_user'
#        print action.response
#        print action.content
if __name__ == "__main__":
    
    unittest.main()