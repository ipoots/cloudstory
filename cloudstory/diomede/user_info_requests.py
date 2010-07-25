'''
Created on Jul 24, 2010

@author: brianjinwright
'''
from restxl import request
from diomede_requests import ServiceReq

__all__ = [
    'SetUserInfoReq',
    'DeleteUserInfoReq',
    'GetEmailAddressReq',
    'AddEmailAddressReq',
    'DeleteEmailAddressReq',
    'SetPrimeEmailReq'
    ]
class SessionTokenReq(ServiceReq):
    session_token = request.CharPathVariable(1,required=True)

class UserReq(SessionTokenReq):
    user = request.CharPathVariable(2,default_value='user')
    
    
class SetUserInfoReq(SessionTokenReq):
    last_name = request.CharVariable(verbose_name='lastname')
    first_name = request.CharVariable(verbose_name='firstname')
    company_name = request.CharVariable(verbose_name='companyname')
    website_url = request.CharVariable(verbose_name='websiteurl')
    phone = request.CharVariable()
    card_name = request.CharVariable(verbose_name='cardname')
    card_number = request.CharVariable(verbose_name='cardnumber')
    card_expiry_year = request.CharVariable(verbose_name='cardexpiryyear')
    card_expiry_month = request.CharVariable(verbose_name='cardexpirymonth')
    card_cvv2 = request.CharVariable(verbose_name='cardcvv2')
    card_address1 = request.CharVariable(verbose_name='cardaddress1')
    card_address2 = request.CharVariable(verbose_name='cardaddress2')
    card_city = request.CharVariable(verbose_name='cardcity')
    card_state = request.CharVariable(verbose_name='cardstate')
    card_zip = request.CharVariable(verbose_name='cardzip')
    card_country = request.CharVariable(verbose_name='cardcountry')
    
    class Meta(SessionTokenReq.Meta):
        method = 'PUT'
        response_type = 'raw'
   
class DeleteUserInfoReq(UserReq):
    info_type = request.CharPathVariable(3,required=True)
    class Meta(UserReq.Meta):
        method = 'DELETE'
        response_type = 'raw' 
        
class GetEmailAddressReq(UserReq):
    email_pv = request.CharPathVariable(3,default_value='email')
    class Meta(GetEmailAddressReq.Meta):
        method = 'GET'
        response_type = 'xml'
        
class AddEmailAddressReq(GetEmailAddressReq):
    email = request.CharPathVariable(4,required=True)
    class Meta(GetEmailAddressReq.Meta):
        method = 'POST'
    
class DeleteEmailAddressReq(AddEmailAddressReq):
    class Meta(AddEmailAddressReq.Meta):
        method = 'DELETE'
        
class SetPrimeEmailReq(GetEmailAddressReq):
    primary = request.CharPathVariable(4,default_value='primary')
    email = request.CharPathVariable(5,required=True)
    
