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
    class Meta(request.Request.Meta):
        request_url = 'https://services.nirvanix.com'
        response_type = 'xml'
    
class SessionTokenReq(NVXRequest):
    """
    Nirvanix Session Token
    """
    sessionToken = request.CharVariable(required=True)
    
    