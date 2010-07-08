'''
Created on Jun 29, 2010

@author: brianjinwright
'''
import unittest
from cloudstory import get_driver
from test_settings import *

class CloudFilesCDNTestCase(unittest.TestCase):
    """CloudFiles Test Case"""

    def setUp(self):
        c_driver = get_driver('cloudfiles')
        self.cf = c_driver(
            CLOUDFILES_AUTH_USER,
            CLOUDFILES_AUTH_KEY
            )
        self.cfb = c_driver(
            CLOUDFILES_B_AUTH_USER,
            CLOUDFILES_B_AUTH_KEY
            ) 
    def testGetCDNContainers(self):
        action = self.cf(
            'get_cdn_containers',
            auth_token=self.cf.auth_token,
            request_url=self.cf.cdn_management_url,
            format='json'
            )
        
        self.assertEquals(action.response.get('status'),'200')
        #TODO: Add this back after we figure out the JSON validation
#        self.failIf(not isinstance(action.content, list), 'Content should be a list')
        actionb = self.cfb(
            'get_cdn_containers',
            auth_token=self.cfb.auth_token,
            request_url=self.cfb.cdn_management_url,
            format='json'
            )
        
        self.failIfEqual(action.response, actionb.response, '''We've got some security issues::Response''')
        self.failIfEqual(action.content, actionb.content, '''We've got some security issues::Content''')

    def testGetCDNContainerInfo(self):
        action = self.cf(
            'get_cdn_container_info',
            auth_token=self.cf.auth_token,
            request_url=self.cf.cdn_management_url,
            request_path=CLOUDFILES_CONTAINER,
            format='json'
            )
        
        
        
