'''
Created on Jul 14, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

__all__ = [
    'CreateFileReq',
    'UploadFileReq'
    ]
class CreateFileReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    l_file = request.CharPathVariable(2,default_value='lfile')
    filename  = request.CharPathVariable(3,required=True)
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class UploadFileReq(ServiceReq):
    file_id = request.CharVariable(required=True,verbose_name='fileid')
    offset = request.CharVariable(required=True)
    buffer_length = request.CharVariable(required=True,verbose_name='bufferLength')
    isComplete = request.CharVariable(required=True)
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    l_file = request.CharPathVariable(2,default_value='lfile')
    upload = request.CharPathVariable(3,default_value='upload')
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'raw'
        
