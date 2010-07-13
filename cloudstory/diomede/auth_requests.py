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
        

class DeleteUserReq(DynamicServiceReq):
    class Meta(DynamicServiceReq.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class ChangePasswordReq(DynamicServiceReq):
    old_password = request.CharVariable(required=True,verbose_name='oldPassword')
    new_password = request.CharVariable(required=True,verbose_name='newPassword')

    class Meta(DynamicServiceReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class ResetPasswordReq(DynamicServiceReq):
    class Meta(DynamicServiceReq.Meta):
        method = 'DELETE'
        
class LoginReq(DynamicServiceReq):
    password = request.CharVariable(required=True)
    class Meta(DynamicServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class LogoutReq(DynamicServiceReq):
    class Meta(DynamicServiceReq.Meta):
        method = 'DELETE'