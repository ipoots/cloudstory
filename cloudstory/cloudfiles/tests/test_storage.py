'''
Created on Jun 29, 2010

@author: brianjinwright
'''
import unittest
from test_settings import\
CLOUDFILES_AUTH_KEY,CLOUDFILES_AUTH_USER,\
CLOUDFILES_CONTAINER,CLOUDFILES_NEW_CONTAINER,\
CLOUDFILES_B_AUTH_USER,CLOUDFILES_B_AUTH_KEY,\
CLOUDFILES_DELETE_OBJECT,CLOUDFILES_DELETE_OBJECT_B 


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
        self.assertEquals(action.response.get('status'),'201')
        self.failIf(
            CLOUDFILES_CONTAINER in actionb.response.get('content-location'),
            'The CLOUDFILES_CONTAINER is in the response of the list_containers')
    
    def testXDeleteContainer(self):
        action = self.cf(
            'delete_container',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path=CLOUDFILES_NEW_CONTAINER
            )
        self.assertEquals(action.response.get('status'),'204')
        
    def testXDeleteObject(self):
        action = self.cf(
            'delete_object',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path='%s/%s' % (CLOUDFILES_CONTAINER,CLOUDFILES_DELETE_OBJECT)
            )
        self.assertEquals(action.response.get('status'),'204')
        
    def testObjectMetaHeaders(self):
        action = self.cf(
            'object_metadata_headers',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path='%s/%s' % (CLOUDFILES_CONTAINER,CLOUDFILES_DELETE_OBJECT)
            )
        self.assertEquals(action.response.get('status'),'204')
        self.failIf(
            not action.response.has_key(
                'content-type'),
            'Response doesn not have content-type')
        actionb = self.cf(
            'object_metadata_headers',
            auth_token=self.cf.auth_token,
            request_url=self.cf.storage_url,
            request_path='%s/%s' % (CLOUDFILES_CONTAINER,CLOUDFILES_DELETE_OBJECT_B)
            )
        self.assertEquals(actionb.response.get('status'),'204')
        self.failIf(
            not actionb.response.has_key(
                'content-type'),
            'Response doesn not have content-type')
        self.failIf(
            action.response.get('etag') == actionb.response.get('etag'),
            'It is looking at the same file check your delete object settings.')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()