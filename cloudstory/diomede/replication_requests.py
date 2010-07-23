'''
Created on Jul 23, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

class ReplicateFile(ServiceReq):
    #Path variables
    session_token = request.CharPathVariable(1,required=True)
    pfile = request.CharPathVariable(2,default_value='pfile')
    file_id = request.CharPathVariable(3,required=True)
    
    #variables
    storage_type_id = request.CharVariable(required=True)
    expiration_date = request.CharVariable(required=True,verbose_name='expirationdate')
    
    class Meta(ServiceReq.Meta):
        response_type = 'xml'
        method = 'POST'
        
