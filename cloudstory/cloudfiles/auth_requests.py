'''
Created on Jun 27, 2010

@author: brianjinwright
'''
from restxl import request
from cloudfiles_requests import AuthTokenReq
__all__ = [
    'LoginReq']
class LoginReq(request.Request):
    '''
    Log into to your CloudFiles account
    '''
    auth_user = request.CharHeader(required=True,verbose_name='X-Auth-User')
    auth_key = request.CharHeader(required=True,verbose_name='X-Auth-Key')
    
    class Meta(request.Request.Meta):
        response_type = 'raw'
        request_url = 'https://auth.api.rackspacecloud.com'
        request_path = '/v1.0'
