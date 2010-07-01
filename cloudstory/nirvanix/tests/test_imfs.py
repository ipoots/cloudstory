'''
Created on Jun 24, 2010

@author: brianjinwright
'''
import unittest
from test_settings import \
NIRVANIX_USERNAME, NIRVANIX_PASSWORD,\
NIRVANIX_APPKEY

from cloudstory.nirvanix import Nirvanix


class TestIMFS(unittest.TestCase):


    def setUp(self):
        self.nvx = Nirvanix(
            NIRVANIX_USERNAME,
            NIRVANIX_PASSWORD,
            NIRVANIX_APPKEY
            )
        
    def test_copy_files(self):
        action = self.nvx(
            'copy_files',
            sessionToken=self.nvx.session_key,
            srcFilePath='/ipoots.png',
            destFolderPath='restXLTest'
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        
    def test_copy_folders(self):
        action = self.nvx(
            'copy_folders',
            sessionToken=self.nvx.session_key,
            srcFolderPath='/restXLTest',
            destFolderPath='/restXLTestTest'
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        
    def test_create_folders(self):
        action = self.nvx(
            'create_folders',
            sessionToken=self.nvx.session_key,
            folderPath='/restXLTestTestTest',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    
    def test_list_folder(self):
        action = self.nvx(
            'list_folder',
            sessionToken=self.nvx.session_key,
            folderPath='/restXLTest',
            pageNumber='1',
            pageSize='10'
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_get_path_info(self):
        action = self.nvx(
            'get_path_info',
            sessionToken=self.nvx.session_key,
            itemPath='/ipoots.png',
            showMetadata='true',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        self.assertEquals(action.content.GetPathInfo.ItemName._,'ipoots.png')
        self.assertEquals(action.content.GetPathInfo.IsFile._,'true')
        self.assertEquals(action.content.GetPathInfo.FileType._,'Image')
        
    def test_move_files(self):
        action = self.nvx(
            'move_files',
            sessionToken=self.nvx.session_key,
            srcFilePath='restXLTest/ipoots.png',
            destFolderPath='restXLTestTest',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_move_folders(self):
        action = self.nvx(
            'move_folders',
            sessionToken=self.nvx.session_key,
            srcFolderPath='restXLTestTest',
            destFolderPath='restXLTestTestTest',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_rename_file(self):
        action = self.nvx(
            'rename_file',
            sessionToken=self.nvx.session_key,
            filePath='restXLTestTestTest/restXLTestTest/ipoots.png',
            newFileName='ipoots-b.png',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_rename_folder(self):
        action = self.nvx(
            'rename_folder',
            sessionToken=self.nvx.session_key,
            folderPath='restXLTestTestTest/restXLTestTest',
            newFolderName='restXLTestTestRenameFolders',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_get_download_nodes(self):
        action = self.nvx(
            'get_download_nodes',
            sessionToken=self.nvx.session_key,
            filePath='ipoots.png',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    
    def test_get_optimal_url(self):
        action = self.nvx(
            'get_optimal_url',
            sessionToken=self.nvx.session_key,
            filePath='ipoots.png',
            expiration='300',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        
    def test_get_storage_node_extended(self):
        action = self.nvx(
            'get_storage_node_extended',
            sessionToken=self.nvx.session_key,
            sizeBytes='9999999',
            destFolderPath='/',
            )
        self.assertEquals(action.content.ResponseCode._,'0')

    def test_get_storage_node(self):
        action = self.nvx(
            'get_storage_node',
            sessionToken=self.nvx.session_key,
            sizeBytes='9999999',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_search_file_system(self):
        action = self.nvx(
            'search_file_system',
            sessionToken=self.nvx.session_key,
            username=NIRVANIX_USERNAME,
            searchTerm='ipoots',
            minFileSize='1',
            maxFileSize='99999999',
            minCreatedDate='1/1/2007',
            maxCreatedDate='1/1/2010',
            maxResults='100',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_sideload(self):
        action = self.nvx(
            'sideload',
            sessionToken=self.nvx.session_key,
            targetURL='http://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.min.js',
            destFilePath='/restXLTestTestTest/jquery.js',
            callbackURL='http://www.example.com',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
    def test_xdelete_folders(self):
        action = self.nvx(
            'delete_folders',
            sessionToken=self.nvx.session_key,
            folderPath='/restXLTestTestTest',
            )
        self.assertEquals(action.content.ResponseCode._,'0')
        actionb = self.nvx(
            'delete_folders',
            sessionToken=self.nvx.session_key,
            folderPath='/restXLTest',
            )
        self.assertEquals(actionb.content.ResponseCode._,'0')
    
    def tearDown(self):
        self.nvx.logout()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()