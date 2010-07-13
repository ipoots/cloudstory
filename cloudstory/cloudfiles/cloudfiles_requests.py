'''
Created on Jun 27, 2010

@author: brianjinwright
'''
from restxl import request
try:
    import json
except:
    try:
        import simplejson as json
    except:
        raise ImportError('json or simplejson must be installed')
__all__ = [
    'CloudFilesResponseError',
    'AuthTokenReq', 
    'DynamicAuthTokenReq', 
    'StorageAccountServicesReq'  
    ]

class CloudFilesResponseError(Exception):
    def __init__(self,value,error_message):
        self.value = value
        self.error_message = error_message
    def __str__(self):
        return repr("Response Code: %s Error Message: %s" % \
                    (self.value, self.error_message))


class AuthTokenReq(request.Request):
    """
    CloudFiles Auth Token Request
    """
    auth_token = request.CharHeader(required=True,verbose_name='X-Auth-Token')
    
class DynamicAuthTokenReq(request.DynamicRequest):
    """
    CloudFiles Auth Token Request
    """
    auth_token = request.CharHeader(required=True,verbose_name='X-Auth-Token')    
    
class StorageAccountServicesReq(DynamicAuthTokenReq):
    limit = request.CharVariable()
    marker = request.CharVariable()
    format = request.CharVariable()
    
    class Meta:
        response_type = 'json'
    
    
    