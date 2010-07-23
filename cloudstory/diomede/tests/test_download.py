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
        
    
    def testGetDownloadURL(self):
        action = self.di('get_download_url',
            session_token=self.di.session_token,
            max_downloads='1',
            error_redirect=ERROR_REDIRECT_URL,
            file_id=FILE_ID)
        self.assertTrue(hasattr(action.content.url, '_'))
        self.assertEquals(action.response.get('status'),'200')
        
#    def testDownload(self):
#        action = self.di('download',
#            session_token=self.di.session_token,
#            file_id=FILE_ID)
#        
#        self.assertEquals(action.response.get('status'),'302')
        
if __name__ == "__main__":
    unittest.main()