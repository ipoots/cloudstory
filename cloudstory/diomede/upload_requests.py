'''
Created on Jul 14, 2010

@author: brianjinwright
'''
from restxl import request

class CreateFileReq(request.DynamicRequest):
    class Meta(request.DynamicRequest.Meta):
        method = 'GET'
        response_type = 'xml'
        
class UploadFileReq(request.DynamicRequest):
    file_id = request.CharVariable(required=True,verbose_name='fileid')
    offset = request.CharVariable(required=True)
    buffer_length = request.CharVariable(required=True,verbose_name='bufferLength')
    isComplete = request.CharVariable(required=True)
    
    class Meta(request.DynamicRequest.Meta):
        method = 'POST'
        response_type = 'raw'
        
