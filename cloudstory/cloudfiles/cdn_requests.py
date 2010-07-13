from restxl import request
from cloudfiles_requests import *

__all__ = [
    'GetCDNContainers',
    'GetCDNContainerInfo',
    'IntializeCDNContainer',
    'EditCDNContainerInfo'
    ]

class GetCDNContainers(DynamicAuthTokenReq):
    enabled_only = request.CharVariable()
    limit = request.CharVariable()
    marker = request.CharVariable()
    format = request.CharVariable()
    class Meta:
        response_type = 'json'
        method = 'GET'
        

class GetCDNContainerInfo(DynamicAuthTokenReq):
    class Meta(DynamicAuthTokenReq.Meta):
        method = 'HEAD'
        response_type = 'raw'
        
class IntializeCDNContainer(DynamicAuthTokenReq):
    ttl = request.CharHeader(verbose_name='X-TTL')
    log_retention = request.CharHeader(verbose_name='X-Log-Retention')
    class Meta(DynamicAuthTokenReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class EditCDNContainerInfo(IntializeCDNContainer):
    cdn_enabled = request.CharHeader(verbose_name='X-CDN-Enabled')
    class Meta(IntializeCDNContainer.Meta):
        method = 'POST'
        