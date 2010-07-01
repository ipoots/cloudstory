'''
Cloudstory Nirvanix Transfer Namespace Requests
Created on Mar 25, 2010

@author: brianjinwright
'''

from nvx_requests import NVXRequest
from restxl import request

class HttpUploadReq(NVXRequest):
    """
    Nirvanix Http Upload Request
    """
    uploadToken = request.CharVariable(required=True)
    destFolderPath = request.CharVariable(required=True)
    forwardingUrl = request.CharVariable()
    callbackURL = request.CharVariable()
    
    class Meta(NVXRequest.Meta):
        request_path = ''
        method = 'POST'
        
