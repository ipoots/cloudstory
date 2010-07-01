'''
Created on Jun 27, 2010

@author: brianjinwright
'''
import unittest
from test_settings import \
NIRVANIX_USERNAME, NIRVANIX_PASSWORD,\
NIRVANIX_APPKEY

from cloudstory.nirvanix import Nirvanix


class TestSharing(unittest.TestCase):


    def setUp(self):
        self.nvx = Nirvanix(
            NIRVANIX_USERNAME,
            NIRVANIX_PASSWORD,
            NIRVANIX_APPKEY
            )
        
    def test_list_hosted_items(self):
        action = self.nvx(
            'list_hosted_items',
            sessionToken=self.nvx.session_key,
            pageNumber='1',
            pageSize='10'
            )
        self.assertEquals(action.content.ResponseCode._,'0')

    def test_create_hosted_item(self):
        action = self.nvx(
            'create_hosted_item',
            sessionToken=self.nvx.session_key,
            sharePath='ipoots.png',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        
    def test_remove_hosted_item(self):
        action = self.nvx(
            'remove_hosted_item',
            sessionToken=self.nvx.session_key,
            sharePath='ipoots.png',
            )
        self.assertEquals(action.content.ResponseCode._,'0')

    def tearDown(self):
        self.nvx.logout()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()