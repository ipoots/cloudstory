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
    container = request.CharPathVariable(1,required=True)

class ListContainerObjects(ListContainers):
    container = request.CharPathVariable(1,required=True)


class CreateContainer(ContainerInfo):
    class Meta(ContainerInfo.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class DeleteContainer(ContainerInfo):
    class Meta(ContainerInfo.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class DeleteObject(DeleteContainer):
    cf_object = request.CharPathVariable(2,required=True)

class ObjectMetaHeaders(AccountInfo):
    container = request.CharPathVariable(1,required=True)
    cf_object = request.CharPathVariable(2,required=True)

class ObjectInfo(ObjectMetaHeaders):
    class Meta(ObjectMetaHeaders.Meta):
        method = 'GET'
        
class CreateMetadata(ObjectMetaHeaders):
    class Meta(ObjectMetaHeaders.Meta):
        method = 'POST'
        