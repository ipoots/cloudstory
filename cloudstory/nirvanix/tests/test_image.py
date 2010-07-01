'''
Created on Jun 27, 2010

@author: brianjinwright
'''
import unittest
from test_settings import \
NIRVANIX_USERNAME, NIRVANIX_PASSWORD,\
NIRVANIX_APPKEY

from cloudstory.nirvanix import Nirvanix


class TestImage(unittest.TestCase):

    def setUp(self):
        self.nvx = Nirvanix(
            NIRVANIX_USERNAME,
            NIRVANIX_PASSWORD,
            NIRVANIX_APPKEY
            )
        try:
            self.nvx(
                'create_folders',
                sessionToken=self.nvx.session_key,
                folderPath='RestXLTest')
        except:
            pass
    def test_resize_image(self):
        action = self.nvx(
            'resize_image',
            sessionToken=self.nvx.session_key,
            srcFilePath='/ipoots.png',
            destFilePath='/RestXLTest/ipoots.png',
            width='100',
            height='100'
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    
    def test_rotate_flip(self):
        action = self.nvx(
            'rotate_flip',
            sessionToken=self.nvx.session_key,
            srcFilePath='/ipoots.png',
            destFilePath='/RestXLTest/ipoots-rotate-flip.png',
            rotate='Rotate90',
            flip='FlipVertical'
            )
        self.assertEquals(action.content.ResponseCode._,'0')

    def tearDown(self):
        self.nvx(
            'delete_folders',
            sessionToken=self.nvx.session_key,
            folderPath='RestXLTest')
        self.nvx.logout()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()