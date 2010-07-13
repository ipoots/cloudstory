'''
Created on Jul 12, 2010

@author: brianjinwright
'''
from restxl import request
__all__ = [
    'ServiceReq',
    'TransferReq',
    'DynamicServiceReq',
    'DynamicTransferReq']
class ServiceReq(request.Request):
    class Meta(request.Request.Meta):
        request_url = 'https://rest.diomedestorage.com/1.1/Service.svc/'
    
class TransferReq(request.Request):
    class Meta(request.Request.Meta):
        request_url = 'https://rest.diomedestorage.com/1.1/Transfer.svc/'
        
class DynamicServiceReq(request.DynamicRequest):
    class Meta(request.DynamicRequest.Meta):
        request_url = 'https://rest.diomedestorage.com/1.1/Service.svc/'
        
class DynamicTransferReq(request.DynamicRequest):
    class Meta(request.DynamicRequest.Meta):
        request_url = 'https://rest.diomedestorage.com/1.1/Transfer.svc/'
        

        