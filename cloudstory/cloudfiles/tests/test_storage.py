'''
Created on Jun 29, 2010

@author: brianjinwright
'''
import unittest
from test_settings import\
CLOUDFILES_AUTH_KEY,CLOUDFILES_AUTH_USER,\
CLOUDFILES_CONTAINER,CLOUDFILES_NEW_CONTAINER,\
CLOUDFILES_B_AUTH_USER,CLOUDFILES_B_AUTH_KEY 


from cloudstory.cloudfiles import CloudFiles


class CloudFilesAuthTestCase(unittest.TestCase):
    """Nirvanix Auth Test Case"""

    def setUp(self):
        self.cf = CloudFiles(
            CLOUDFILES_AUTH_USER,
            CLOUDFILES_AUTH_KEY
            )
        self.cfb = CloudFiles(
            CLOUDFILES_B_AUTH_USER,
            CLOUDFILES_B_AUTH_KEY
            ) 

    def testListContainers(self):
        action = self.cf(
            'list_containers',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            format='json'
            )
        self.assertEquals(action.response.get('status'),'200')
        self.failIf(not isinstance(action.content, list), 'Content should be a list')
        actionb = self.cfb(
            'list_containers',
            auth_token=self.cfb.auth_token,
            request_url=self.cfb.storage_url,
            format='json'
            )

        
        self.failIfEqual(action.response, actionb.response, '''We've got some security issues::Response''')
        self.failIfEqual(action.content, actionb.content, '''We've got some security issues::Content''')
        
    def testAccountInfo(self):
        action = self.cf(
            'account_info',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            
            )
        
        self.failIf(
            not action.response.has_key(
                'x-account-container-count'),
            'Response doesn not have x-account-container-count')
        
        self.failIf(
            not action.response.has_key(
                'x-account-bytes-used'),
            'Response doesn not have x-account-bytes-used')

    def testContainerInfo(self):
        action = self.cf(
            'container_info',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path=CLOUDFILES_CONTAINER
            )

        self.failIf(
            not action.response.has_key(
                'x-container-object-count'),
            'Response doesn not have x-account-container-count')
        
        self.failIf(
            not action.response.has_key(
                'x-container-bytes-used'),
            'Response doesn not have x-account-bytes-used')

    def testContainerObjectsInfo(self):
        action = self.cf(
            'list_container_objects',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path=CLOUDFILES_CONTAINER,
            format='json'
            )
        self.failIf(not isinstance(action.content, list), 'Content should be a list')
        
    def testCreateContainer(self):
        action = self.cf(
            'create_container',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path=CLOUDFILES_NEW_CONTAINER,
            )
        actionb = self.cf(
            'list_containers',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            
            format='json'
            )
        self.assertEquals(action.response.get('status'),'202')
        self.failIf(
            CLOUDFILES_CONTAINER in actionb.response.get('content-location'),
            'The CLOUDFILES_CONTAINER is in the response of the list_containers')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()