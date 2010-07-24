'''
Created on Jul 23, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

class CreateFileMetaDataReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    lfile = request.CharPathVariable(3,default_value='lfile')
    file_id = request.CharPathVariable(4,required=True)
    #Variables
    meta_name = request.CharVariable(required=True,verbose_name='metaname')
    meta_value = request.CharVariable(required=True,verbose_name='metavalue')
    
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'xml'
        
class GetFileMetaData(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    lfile = request.CharPathVariable(3,default_value='lfile')
    file_id = request.CharPathVariable(4,required=True)
    
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class SetFileMetadataReq(GetFileMetaData):
    class Meta(GetFileMetaData.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class DeleteFileMetadataReq(GetFileMetaData):
    class Meta(GetFileMetaData.Meta):
        method = 'DELETE'
        
class CreateMetaDataReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    meta_name = request.CharPathVariable(3,required=True)
    meta_value = request.CharPathVariable(4,required=True)
    
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'xml'
        
class GetMetaDataReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    #Variables
    metadata_id = request.CharVariable(verbose_name='metadataid')
    meta_name = request.CharVariable(verbose_name='metaname')
    meta_value = request.CharVariable(verbose_name='metavalue')
    
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'

class EditMetaDataReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    metadata_id = request.CharPathVariable(3,required=True)
    #Variables
    meta_name = request.CharVariable(verbose_name='metaname')
    meta_value = request.CharVariable(verbose_name='metavalue')
    
    class Meta(ServiceReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class DeleteMetaDataReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    metadata = request.CharPathVariable(2,default_value='metadata')
    metadata_id = request.CharPathVariable(3,required=True)
    
    class Meta(ServiceReq.Meta):
        method = 'DELETE'
        response_type = 'raw'