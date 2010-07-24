'''
Created on Jul 24, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

class GetAllProductsReq(ServiceReq):
    products = request.CharPathVariable(1,default='products')
    
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class SessionTokenReq(ServiceReq):
    session_token = request.CharPathVariable(1,required=True)
    
class GetMyProductsReq(SessionTokenReq):
    products = request.CharPathVariable(2,default='products')
    
    class Meta(SessionTokenReq.Meta):
        method = 'GET'
        response_type = 'raw'

class PurchaseProductReq(GetMyProductsReq):
    product_id = request.CharPathVariable(3,required=True)
    
    class Meta(GetMyProductsReq.Meta):
        method = 'PUT'

class CancelProductReq(PurchaseProductReq):
    class Meta(PurchaseProductReq.Meta):
        method = 'DELETE'
        
class GetAllContactsReq(ServiceReq):
    contracts = request.CharPathVariable(2,default_value='contracts')
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class PurchaseContractReq(SessionTokenReq,GetAllContactsReq):
    contract_id = request.CharPathVariable(3,required=True)
    
    class Meta(SessionTokenReq.Meta):
        method = 'PUT'
        response_type = 'xml'
        
class CancelContract(PurchaseContractReq):
    class Meta(PurchaseContractReq):
        method = 'DELETE'
        response_type = 'raw'

    