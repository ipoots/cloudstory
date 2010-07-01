'''
Nirvanix Authentication Requests

All Nirvanix API methods related to the authentication namespace. 
This module requires RestXL REST client library. 
'''
from restxl import request
from cloudstory.nirvanix.nvx_requests import NVXRequest, SessionTokenReq
__all__ = [
    'LoginReq',
    'LoginProxyReq',
    'LogoutReq',
    'ChangePasswordReq',
    'SetChildAccountPasswordReq'    
    ]
NIRVANIX_SERVICES_URL = 'https://services.nirvanix.com'

class BaseAuthReq(NVXRequest):
    appKey = request.CharVariable(required=True)
    username = request.CharVariable(required=True)
    
    class Meta:
        request_url = NIRVANIX_SERVICES_URL
    
class LoginReq(BaseAuthReq):
    """
    Nirvanix Login Request
    """
    password = request.CharVariable(required=True)
    
    class Meta(BaseAuthReq.Meta):
        request_path = '/ws/Authentication/Login.ashx'
        
class LoginProxyReq(LoginReq):
    """
    Nirvanix Login Proxy Request
    """
    consumerIP = request.CharVariable(required=True)
    
    class Meta(LoginReq.Meta):
        request_path = '/ws/Authentication/LoginProxy.ashx'
        
        
class LogoutReq(SessionTokenReq):
    """
    Nirvanix Logout Request
    """
    class Meta(SessionTokenReq.Meta):
        request_path = '/ws/Authentication/Logout.ashx'
        
class ChangePasswordReq(BaseAuthReq):
    """
    Nirvanix Change Password Request
    """
    oldPassword = request.CharVariable(required=True)
    newPassword = request.CharVariable(required=True)
    
    class Meta(BaseAuthReq.Meta):
        request_path = '/ws/Authentication/ChangePassword.ashx'
        
class SetChildAccountPasswordReq(LoginReq):
    childAccountUsername = request.CharVariable(required=True)
    childAccountPassword = request.CharVariable(required=True)
    
    class Meta(LoginReq.Meta):
        request_path = '/ws/Authentication/SetChildAccountPassword.ashx'
        
