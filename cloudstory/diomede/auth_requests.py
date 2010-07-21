'''
Created on Jul 12, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import *
__all__ = [
    'CreateUserReq',
    'DeleteUserReq',
    'ChangePasswordReq',
    'ResetPasswordReq',
    'LoginReq',
    'LogoutReq',
    ]

class CreateUserReq(ServiceReq):
    '''
    Create a Diomede User
    '''
    username = request.CharVariable(required=True)
    password = request.CharVariable(required=True)
    email = request.CharVariable(required=True)
    
    class Meta(ServiceReq.Meta):
        response_type = 'raw'
        method = 'POST'
        
class DeleteUserReq(ServiceReq):
    session_token = request.CharPathVariable(1,required=True)
    user = request.CharPathVariable(2,default_value='user')
    class Meta(ServiceReq.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class ChangePasswordReq(ServiceReq):
    old_password = request.CharVariable(required=True,verbose_name='oldPassword')
    new_password = request.CharVariable(required=True,verbose_name='newPassword')

    class Meta(ServiceReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class ResetPasswordReq(ServiceReq):
    class Meta(ServiceReq.Meta):
        method = 'DELETE'
        
class LoginReq(ServiceReq):
    username = request.CharPathVariable(1,required=True)
    password = request.CharVariable(required=True)
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class LogoutReq(ServiceReq):
    class Meta(ServiceReq.Meta):
        method = 'DELETE'