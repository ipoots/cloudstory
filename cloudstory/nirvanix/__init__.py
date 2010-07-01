from auth_requests import *
from imfs_requests import *
from metadata_requests import *
from sharing_requests import *
from image_requests import *
from restxl.client import RestXLer
NIRVANIX_SERVICES_URL = 'https://services.nirvanix.com'

NIRVANIX_APP_KEY = None

NIRVANIX_PASSWORD = None

NIRVANIX_USERNAME = None

                    
class Nirvanix(RestXLer):
    def __init__(self,
                 username=None,
                 password=None,
                 app_key=None,
                 session_key=None,
                 proxy_addr=None,):
        self.username = username
        self.password = password
        self.app_key = app_key
        if proxy_addr:
            self.proxy_addr = proxy_addr
        if session_key:
            self.session_key = session_key
        else:
            tt = self.login()
            if tt.content.ResponseCode._ == '0':
                self.session_key = tt.content.SessionToken._
            
#    START AUTHENTICATION NAMESPACE        
    def login(self):
        """
        Login
        Doc URL: http://developer.nirvanix.com/sitefiles/1000/API.html#_Toc175999910
        """
        cs = LoginReq(
            username=self.username,
            password=self.password,
            appKey=self.app_key)
        tt = cs()
        self.session_key = tt.content.SessionToken._
        return tt
        
    
    def login_proxy(self):
        """
        Login Proxy
        Doc URL: http://developer.nirvanix.com/sitefiles/1000/API.html#_TocLoginProxy
        """
        cs = LoginProxyReq(
            username=self.username,
            password=self.password,
            consumerIP=getattr(self, 'proxy_addr',None))
        tt = cs()
        self.session_key = tt.content.SessionToken._
        return tt
        
    def logout(self,**kwargs):
        """
        Logout
        Doc URL: http://developer.nirvanix.com/sitefiles/1000/API.html#_TocLoginProxy 
        """
        if self.session_key:
            session_token = self.session_key 
            cs = LogoutReq(sessionToken=session_token)
        else:
            cs = LogoutReq(**kwargs)
        tt = cs()
        return tt    
    change_password = ChangePasswordReq
        
    set_child_account_password = SetChildAccountPasswordReq
        

#    END AUTHENTICATION NAMESPACE

#    START Internet Media File System (IMFS) Namespace
    
    copy_files = CopyFilesReq
    
    copy_folders = CopyFoldersReq
     
    create_folders = CreateFoldersReq
    
    delete_files = DeleteFilesReq
    
    delete_folders = DeleteFoldersReq
    
    get_path_info = GetPathInfoReq
    
    list_folder = ListFolderReq
        
    move_files = MoveFilesReq
    
    move_folders = MoveFoldersReq
    
    rename_file = RenameFileReq
    
    rename_folder = RenameFolderReq

    get_download_nodes = GetDownloadNodesReq
        
    get_optimal_url = GetOptimalUrlsReq
        
    get_storage_node_extended = GetStorageNodeExtendedReq
        
    get_storage_node = GetStorageNodeReq 
        
    search_file_system = SearchFileSystemReq 
                
    sideload = SideloadReq 

#    END Internet Media File System (IMFS) Namespace

#    START Metadata Namespace
    delete_all_metadata = DeleteAllMetadataReq 
        
    get_meta_data = GetMetadataReq
        
    set_metadata = SetMetadataReq 
    
    delete_all_tags = DeleteAllTagsReq
    
    delete_tags = DeleteTagsReq 
        
    get_tags = GetTagsReq
    
    set_tags = SetTagsReq 
    
    search_metadata = SearchMetadataReq
    
    search_tags = SearchTagsReq 
    
#    END Metadata Namespace

#    START Sharing Namespace
    list_hosted_items = ListHostedItemsReq 
    
    create_hosted_item = CreateHostedItemReq
    
    remove_hosted_item = RemoveHostedItemReq
    
#    END Sharing Namespace

#    START Image Namespace

    resize_image = ResizeReq 
    
    rotate_flip = RotateFlipReq 

#    END Image Namespace

