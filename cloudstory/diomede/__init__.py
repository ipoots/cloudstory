from restxl.client import RestXLer
from auth_requests import *
from download_requests import *
class Diomede(RestXLer):
    def __init__(self,
                 username=None,
                 password=None,
                 session_token=None):
        self.username = username
        self.password = password

        if session_token:
            self.session_token = session_token
        else:
            tt = self.login()
            self.session_token = getattr(tt.content.sessionToken, '_',None)
            
    def login(self):
        cs = LoginReq(
            username=self.username,
            password=self.password,
            )
        tt = cs()
        self.session_token = tt.content.sessionToken._
        return tt
        
    create_user = CreateUserReq
    delete_user = DeleteUserReq
    change_password = ChangePasswordReq
    reset_password = ResetPasswordReq
    logout = LogoutReq
    get_download_url = GetDownloadURLReq
    download = DownloadReq