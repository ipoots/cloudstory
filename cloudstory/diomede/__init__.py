from restxl.client import RestXLer
from auth_requests import *

class Diomede(RestXLer):
    create_user = CreateUserReq
    delete_user = DeleteUserReq
    change_password = ChangePasswordReq
    reset_password = ResetPasswordReq
    logout = LogoutReq