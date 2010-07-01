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
    'CreateContainer'
    ]

class StorageAccountServicesReq(DynamicAuthTokenReq):
    limit = request.CharVariable()
    marker = request.CharVariable()
    format = request.CharVariable()
    
    class Meta(DynamicAuthTokenReq.Meta):
        response_type = 'json'
        
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
        