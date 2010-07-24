'''
Created on Jul 23, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

class CreateRepPolicyReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    replication_policy = request.CharPathVariable(2,default_value='replicationpolicy')
    
    #Variables
    default_online = request.CharVariable(verbose_name='defaultonline')
    default_nearline = request.CharVariable(verbose_name='defaultnearline')
    default_offline = request.CharVariable(verbose_name='defaultoffline')
    trigger_hours = request.CharVariable(verbose_name='triggerhours')
    trigger_online = request.CharVariable(verbose_name='triggeronline')
    trigger_nearline = request.CharVariable(verbose_name='triggernearline')
    trigger_offline = request.CharVariable(verbose_name='triggeroffline')
    expire_hours = request.CharVariable(verbose_name='expirehours')
    
    class Meta(ServiceReq.Meta):
        method = 'POST'
        response_type = 'xml'
        
class GetRepPoliciesReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    replication_policy = request.CharPathVariable(1,default_value='replicationpolicy')
    
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class EditRepPolicyReq(GetRepPoliciesReq):
    #Path Variables
    policy_id = request.CharPathVariable(3,required=True)
    
    default_online = request.CharVariable(verbose_name='defaultonline')
    default_nearline = request.CharVariable(verbose_name='defaultnearline')
    default_offline = request.CharVariable(verbose_name='defaultoffline')
    trigger_hours = request.CharVariable(verbose_name='triggerhours')
    trigger_online = request.CharVariable(verbose_name='triggeronline')
    trigger_nearline = request.CharVariable(verbose_name='triggernearline')
    trigger_offline = request.CharVariable(verbose_name='triggeroffline')
    expire_hours = request.CharVariable(verbose_name='expirehours')
    
    class Meta(GetRepPoliciesReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class DeleteRepPolicyReq(GetRepPoliciesReq):
    #Path Variables
    policy_id = request.CharPathVariable(3,required=True)
    
    class Meta(GetRepPoliciesReq.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class SetDefaultRepPolicyReq(GetRepPoliciesReq):
    default = request.CharPathVariable(1,default_value='default')
    policy_id = request.CharVariable(required=True,verbose_name='policyid')
    
    class Meta(SetDefaultRepPolicyReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
class GetDefaultRepPolicyReq(GetRepPoliciesReq):
    default = request.CharPathVariable(1,default_value='default')
    
    class Meta(GetDefaultRepPolicyReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class SetRepPolicyReq(GetRepPoliciesReq):
    lfile = request.CharPathVariable(3,default_value='lfile')
    class Meta(GetRepPoliciesReq.Meta):
        method = 'PUT'
        response_type = 'raw'
    
    
    