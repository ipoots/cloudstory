'''
Created on Jul 14, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import DynamicServiceReq
class GetDownloadURLReq(DynamicServiceReq):
    max_downloads = request.CharVariable(required=True,verbose_name='maxDownloads')
    error_redirect = request.CharVariable(required=True,verbose_name='errorRedirect')
    class Meta(request.DynamicRequest.Meta):
        response_type = 'xml'
        method = 'GET'
        
class DownloadURLReq(DynamicServiceReq):
    class Meta(request.DynamicRequest.Meta):
        response_type = 'xml'
        method = 'GET'
        
