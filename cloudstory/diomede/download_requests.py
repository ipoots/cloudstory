'''
Created on Jul 14, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq
__all__ = [
    'GetDownloadURLReq',
    'DownloadReq'
    ]
class GetDownloadURLReq(ServiceReq):
    max_downloads = request.CharVariable(required=True,verbose_name='maxDownloads')
    error_redirect = request.CharVariable(required=True,verbose_name='errorRedirect')
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    l_file = request.CharPathVariable(2,default_value='lfile')
    url = request.CharPathVariable(3,default_value='url')
    file_id = request.CharPathVariable(4,required=True)
    
    class Meta(ServiceReq.Meta):
        response_type = 'xml'
        method = 'GET'
        
class DownloadReq(ServiceReq):
    session_token = request.CharPathVariable(1,required=True)
    l_file = request.CharPathVariable(2,default_value='lfile')
    file_id = request.CharPathVariable(3,required=True)
    class Meta(ServiceReq.Meta):
        response_type = 'xml'
        method = 'GET'
        
