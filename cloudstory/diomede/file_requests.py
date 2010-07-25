'''
Created on Jul 22, 2010

@author: brianjinwright
'''

from restxl import request
from diomede_requests import ServiceReq
__all__ = [
    'SearchFilesReq',
    'SearchFilesTotalReq',
    'DeleteFileReq',
    'RenameOrDeleteFileReq'
    ]
class SearchFilesReq(ServiceReq):
    #Path Variables
    session_token = request.CharPathVariable(1,required=True)
    lfile = request.CharPathVariable(2,default_value='lfile')
    #Variables
    file_id = request.CharVariable(verbose_name='fileid')
    get_pfs = request.CharVariable(verbose_name='getpfs')
    file_name = request.CharVariable(verbose_name='filename')
    hash_md5 = request.CharVariable(verbose_name='hashmd5')
    hash_sha1 = request.CharVariable(verbose_name='hashsha1')
    min_size = request.CharVariable(verbose_name='minsize')
    max_size = request.CharVariable(verbose_name='maxsize')
    start_date = request.CharVariable(verbose_name='startdate')
    end_date = request.CharVariable(verbose_name='enddate')
    is_deleted = request.CharVariable(verbose_name='isdeleted')
    is_complete = request.CharVariable(verbose_name='iscomplete')
    meta_name = request.CharVariable(verbose_name='metaname')
    meta_value = request.CharVariable(verbose_name='metavalue')
    offset = request.CharVariable()
    page = request.CharVariable()
    
    class Meta(ServiceReq.Meta):
        response_type = 'xml'
        method = 'GET'
        
class SearchFilesTotalReq(ServiceReq):
    #Path variables
    session_token = request.CharPathVariable(1,required=True)
    lfile = request.CharPathVariable(2,default_value='lfile')
    totals = request.CharPathVariable(3,default_value='totals')
    #variables
    file_id = request.CharVariable(verbose_name='fileid')
    hash_md5 = request.CharVariable(verbose_name='hashmd5')
    hash_sha1 = request.CharVariable(verbose_name='hashsha1')
    min_size = request.CharVariable(verbose_name='minsize')
    max_size = request.CharVariable(verbose_name='maxsize')
    start_date = request.CharVariable(verbose_name='startdate')
    end_date = request.CharVariable(verbose_name='enddate')
    is_complete = request.CharVariable(verbose_name='iscomplete')
    meta_name = request.CharVariable(verbose_name='metaname')
    meta_value = request.CharVariable(verbose_name='metavalue')
    
    class Meta(ServiceReq.Meta):
        response_type = 'xml'
        method = 'GET'

class DeleteFileReq(ServiceReq):
    #Path variables
    session_token = request.CharPathVariable(1,required=True)
    lfile = request.CharPathVariable(2,default_value='lfile')
    file_id = request.CharPathVariable(3,required=True)
    
    class Meta(ServiceReq.Meta):
        method = 'DELETE'
        response_type = 'raw'
        
class RenameOrDeleteFileReq(ServiceReq):
    #Path variables
    session_token = request.CharPathVariable(1,required=True)
    lfile = request.CharPathVariable(2,default_value='lfile')
    file_id = request.CharPathVariable(3,required=True)
    #Variables
    file_name = request.CharVariable(verbose_name='filename')
    is_deleted = request.CharVariable(verbose_name='isdeleted')
    
    class Meta(ServiceReq.Meta):
        method = 'PUT'
        response_type = 'raw'
        
