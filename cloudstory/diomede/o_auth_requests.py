'''
Created on Jul 14, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

__all__ = [
    'CreateOAuthReq',
    'GetOAuthSecretKeyReq'
    ]
class CreateOAuthReq(ServiceReq):
    username = request.CharVariable(required=True)
    password = request.CharVariable(required=True)
    #Path Variables
    oauth = request.CharPathVariable(1,default_value='oauth')
    
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'xml'
        
class GetOAuthSecretKeyReq(ServiceReq):
    #Path Variables
    oauth = request.CharPathVariable(1,default_value='oauth')
    oauth_id = request.CharPathVariable(1,required=True)
    
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'xml'