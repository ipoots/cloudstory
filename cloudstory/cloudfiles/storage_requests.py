'''
Created on Jun 29, 2010

@author: brianjinwright
'''
from cloudfiles_requests import *
from restxl import request
__all__ = [
    'ListContainers',
    'AccountInfo',
    'ContainerInfo',
    'ListContainerObjects',
    'CreateContainer',
    'DeleteContainer',
    'DeleteObject',
    'ObjectMetaHeaders',
    'ObjectInfo',
    'CreateMetadata'
    ]

class ListContainers(StorageAccountServicesReq):
    class Meta(StorageAccountServicesReq.Meta):
        method = 'GET'
        
class AccountInfo(DynamicAuthTokenReq):
    class Meta(DynamicAuthTokenReq.Meta):
        method = 'HEAD'
        response_type = 'raw'
        
class ContainerInfo(AccountInfo):
    pass

class ListContainerObjects(ListContainers):
    pass

class CreateContainer(DynamicAuthTokenReq):
    class Meta(DynamicAuthTokenReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class DeleteContainer(DynamicAuthTokenReq):
    class Meta(DynamicAuthTokenReq.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class DeleteObject(DeleteContainer):
    pass

class ObjectMetaHeaders(AccountInfo):
    pass        

class ObjectInfo(AccountInfo):
    class Meta(AccountInfo.Meta):
        method = 'GET'
        response_type = 'raw'
        
class CreateMetadata(AccountInfo):
    class Meta(AccountInfo.Meta):
        method = 'POST'
        response_type = 'raw'