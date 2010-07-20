'''
Cloudstory Nirvanix Metadata Namespace Requests
Created on Mar 24, 2010

@author: brianjinwright
'''
from nvx_requests import SessionTokenReq
from restxl import request
__all__ = [
    'DeleteAllMetadataReq',
    'DeleteMetadataReq',
    'GetMetadataReq',
    'SetMetadataReq',
    'DeleteAllTagsReq',
    'DeleteTagsReq',
    'GetTagsReq',
    'SetTagsReq',
    'SearchMetadataReq',
    'SearchTagsReq'
    ]
class DeleteAllMetadataReq(SessionTokenReq):
    """
    Nirvanix Delete All Metadata Request
    """
    path = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Metadata/DeleteAllMetadata.ashx'
        
class DeleteMetadataReq(DeleteAllMetadataReq):
    """
    Nirvanix Delete All Metadata Request
    """
    metadata = request.CharVariable(required=True)
    
    class Meta(DeleteAllMetadataReq.Meta):
        request_path = 'ws/Metadata/DeleteMetadata.ashx'
        
class GetMetadataReq(DeleteAllMetadataReq):
    """
    Nirvanix Get Metadata Request
    """
    
    class Meta(DeleteAllMetadataReq.Meta):
        request_path = 'ws/Metadata/GetMetadata.ashx'
        
class SetMetadataReq(DeleteMetadataReq):
    """
    Nirvanix Set Metadata Request
    """
    
    class Meta(DeleteMetadataReq.Meta):
        request_path = 'ws/Metadata/SetMetadata.ashx'
        
class DeleteAllTagsReq(DeleteAllMetadataReq):
    """
    Nirvanix Delete All Tags Request
    """
    
    class Meta(DeleteAllMetadataReq.Meta):
        request_path = 'ws/Metadata/DeleteAllTags.ashx'
        
class DeleteTagsReq(DeleteAllMetadataReq):
    """
    Nirvanix Delete Tags Request
    """
    tag = request.CharVariable(required=True)
    
    class Meta(DeleteAllMetadataReq.Meta):
        request_path = 'ws/Metadata/DeleteTags.ashx'
        
class GetTagsReq(DeleteAllMetadataReq):
    """
    Nirvanix Get Tags Request
    """
    
    class Meta(DeleteAllMetadataReq.Meta):
        request_path = 'ws/Metadata/GetTags.ashx'
        
class SetTagsReq(DeleteTagsReq):
    """
    Nirvanix Set Tags Request
    """
    
    class Meta(DeleteTagsReq.Meta):
        request_path = 'ws/Metadata/SetTags.ashx'
        
class SearchMetadataReq(SessionTokenReq):
    """
    Nirvanix Search Metadata Request
    """
    username = request.CharVariable(required=True)
    searchKey = request.CharVariable(required=True)
    searchTerm = request.CharVariable(required=True)
    maxResults = request.CharVariable(required=True)
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Metadata/SearchMetadata.ashx'

class SearchTagsReq(SessionTokenReq):
    """
    Nirvanix Search Tags Request
    """
    username = request.CharVariable(required=True)
    searchTerm = request.CharVariable(required=True)
    maxResults = request.CharVariable(required=True)
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/Metadata/SearchTags.ashx'