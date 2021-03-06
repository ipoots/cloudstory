"""Rackspace CloudFiles"""
from restxl.client import RestXLer
from auth_requests import *
from storage_requests import *
from cdn_requests import *
class CloudFiles(RestXLer):
    
    def __init__(self,
                 auth_user=None,
                 auth_key=None,
                 auth_token=None):
        self.auth_user = auth_user
        self.auth_key = auth_key
        self.auth_token = auth_token
        tt = self.login()
        
#            if tt.ResponseCode._ == '0':
#                self.session_key = tt.SessionToken._
            
#    START AUTHENTICATION NAMESPACE        
    def login(self):
        """
        Login
        """
        cs = LoginReq(
            auth_user=self.auth_user,
            auth_key=self.auth_key)
        tt = cs()
        self.server_management_url = tt.response.get('x-server-management-url')
        self.auth_token = tt.response.get('x-auth-token')
        self.cdn_management_url = tt.response.get('x-cdn-management-url')
        self.storage_token = tt.response.get('x-storage-token')
        self.storage_url = tt.response.get('x-storage-url')   
        return tt
    #Storage Service Requests
    list_containers = ListContainers
    account_info = AccountInfo
    container_info = ContainerInfo
    list_container_objects = ListContainerObjects
    create_container = CreateContainer
    delete_container = DeleteContainer
    delete_object = DeleteObject
    object_metadata_headers = ObjectMetaHeaders
    object_info = ObjectInfo
    create_meta_data = CreateMetadata
    #CDN Service Requests
    get_cdn_containers = GetCDNContainers
    get_cdn_container_info = GetCDNContainerInfo
    initialize_cdn_container = IntializeCDNContainer
    edit_cdn_container_info = EditCDNContainerInfo