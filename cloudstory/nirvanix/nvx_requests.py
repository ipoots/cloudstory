'''
Created on Mar 23, 2010

@author: brianjinwright
'''
from restxl import request

import httplib2
from urllib import urlencode
import urllib2
try:
    import json
except:
    try:
        import simplejson as json
    except:
        raise ImportError('json or simplejson must be installed')
try:
    import simplexmlapi
except:
    raise ImportError('simplexmlapi must be installed')
try:
    from BeautifulSoup import BeautifulSoup
except:
    raise ImportError('beautifulsoup must be installed')

__all__ = [
    'NVXRequest',
    'SessionTokenReq',    
    ]
class NirvanixResponseError(Exception):
    def __init__(self,value,error_message):
        self.value = value
        self.error_message = error_message
    def __str__(self):
        return repr("Response Code: %s Error Message: %s" % \
                    (self.value, self.error_message))
        
class NVXRequest(request.Request):
    def rest_request(self):
        
        method = getattr(self.Meta, 'method','GET')
         
        response_type = getattr(self.Meta, 'response_type','xml')
        if not hasattr(self.Meta, 'request_url'):
            raise request.RestXLRequestError('You must have a request url in the Meta class.')
        
        request_url = getattr(self.Meta, 'request_url') + getattr(self.Meta, 'request_path', '')
        if len(self._urlvars) != 0:
            body = urlencode(self._urlvars)
            if method == 'GET': 
                request_url = '%s?%s' %(request_url,body)
                body = None
        else:
            body = None
        headers = getattr(self, '_headers',{})
        h = httplib2.Http()
        resp, content = h.request(request_url, method=method, body=body,headers=headers)
        
        if response_type == 'xml':
            nd = simplexmlapi.loads(content)
        if response_type == 'json':
            nd = json.loads(content)
        if response_type == 'html':
            nd = BeautifulSoup(content)
        if response_type == 'raw':
            nd = content
        if nd.ResponseCode._ != '0':
            raise NirvanixResponseError(
                nd.ResponseCode._,
                nd.ErrorMessage._)
            
        return request.RestXLResponse(resp,nd)
    
    class Meta(request.Request.Meta):
        request_url = 'https://services.nirvanix.com'
    
class SessionTokenReq(NVXRequest):
    """
    Nirvanix Session Token
    """
    sessionToken = request.CharVariable(required=True)
    
    