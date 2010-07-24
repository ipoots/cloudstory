'''
Created on Jul 24, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

class SessionLogsReq(ServiceReq):
    session_token = request.CharPathVariable(1,required=True)
    logs = request.CharPathVariable(2,default_value='logs')
    start_date = request.CharVariable(verbose_name='startdate')
    end_date = request.CharVariable(verbose_name='enddate')
    class Meta(ServiceReq.Meta):
        method = 'GET'
        response_type = 'xml'
    
class OffsetPagesizeReq(SessionLogsReq):
    offset = request.CharVariable(required=True)
    page_size = request.CharVariable(required=True,verbose_name='pagesize')
        
class SearchLoginLogReq(SessionLogsReq):
    login = request.CharPathVariable(3,default_value='login')
    offset = request.CharVariable()
    page = request.CharVariable()
    ip = request.CharVariable()
        
class SearchInvoiceLogReq(SessionLogsReq):
    invoice = request.CharPathVariable(3,default_value='invoice')
    invoice_status = request.CharVariable(required=True,verbose_name='invoicestatus')
    
class SearchPaymentLogReq(SessionLogsReq):
    payment = request.CharPathVariable(3,default_value='payment')
    
class SearchFilesTotalLogReq(OffsetPagesizeReq):
    lfile = request.CharPathVariable(3,default_value='lfile')
    totals = request.CharPathVariable(4,default_value='totals')
    
class SeachDownloadLogReq(OffsetPagesizeReq):
    download = request.CharPathVariable(3,default_value='download')
    file_id = request.CharVariable(required=True,verbose_name='fileid')
    token = request.CharVariable()
    ip = request.CharVariable()
    
class SearchUploadLogReq(OffsetPagesizeReq):
    upload = request.CharPathVariable(3,default_value='upload')
    file_id = request.CharVariable(required=True,verbose_name='fileid')
    
