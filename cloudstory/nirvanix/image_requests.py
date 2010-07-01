'''
Cloudstory Nirvanix Image Namespace
Created on Mar 25, 2010

@author: brianjinwright
'''
from nvx_requests import SessionTokenReq
from restxl import request
__all__ = [
    'ResizeReq',
    'RotateFlipReq',
    ]
class ResizeReq(SessionTokenReq):
    """
    Nirvanix Resize Request
    """
    srcFilePath = request.CharVariable(required=True)
    destFilePath = request.CharVariable(required=True)
    width = request.CharVariable(required=True)
    height = request.CharVariable(required=True)
    callbackURL = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = '/ws/Image/Resize.ashx'
        
class RotateFlipReq(SessionTokenReq):
    """
    Nirvanix Rotate Flip Request
    """
    srcFilePath = request.CharVariable(required=True)
    destFilePath = request.CharVariable(required=True)
    rotate = request.CharVariable(required=True)
    flip = request.CharVariable(required=True)
    callbackURL = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = '/ws/Image/RotateFlip.ashx'
        