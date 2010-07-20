'''
Cloudstory Nirvanix Sharing Namespace Requests
Created on Mar 24, 2010

@author: brianjinwright
'''
__all__ = [
    'ListHostedItemsReq',
    'CreateHostedItemReq',
    'RemoveHostedItemReq'
    ]

from nvx_requests import SessionTokenReq
from restxl import request

class ListHostedItemsReq(SessionTokenReq):
    """
    Nirvanix List Hosted Items Request
    """
    pageNumber = request.CharVariable(required=True)
    pageSize = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Sharing/ListHostedItems.ashx'
        
class CreateHostedItemReq(SessionTokenReq):
    """
    Nirvanix List Hosted Items Request
    """
    sharePath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Sharing/CreateHostedItem.ashx'
        
class RemoveHostedItemReq(CreateHostedItemReq):
    """
    Nirvanix Remove Hosted Items Request
    """
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Sharing/RemoveHostedItem.ashx'

