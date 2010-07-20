'''
Created on Mar 24, 2010

@author: brianjinwright
'''
from nvx_requests import NVXRequest, SessionTokenReq
from restxl import request

class CopyFilesReq(SessionTokenReq):
    """
    Nirvanix Copy Files Request
    """
    srcFilePath = request.CharVariable(required=True)
    destFolderPath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/CopyFiles.ashx'
        
class CopyFoldersReq(SessionTokenReq):
    """
    Nirvanix Copy Folders Request
    """
    srcFolderPath = request.CharVariable(required=True)
    destFolderPath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/CopyFolders.ashx'
        
class CreateFoldersReq(SessionTokenReq):
    """
    Nirvanix Create Folders Request
    """
    folderPath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/CreateFolders.ashx'
        
class DeleteFilesReq(SessionTokenReq):
    """
    Nirvanix Delete Files Request
    """
    filePath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/DeleteFiles.ashx'
        
class DeleteFoldersReq(SessionTokenReq):
    """
    Nirvanix Delete Folders Request
    """
    folderPath = request.CharVariable(required=True)

    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/DeleteFolders.ashx'
        
class GetPathInfoReq(SessionTokenReq):
    """
    Nirvanix Get Path Info Request
    """
    itemPath = request.CharVariable(required=True)
    showMetadata = request.CharVariable()
    showTags = request.CharVariable()
    showIsShared = request.CharVariable()
    metadataOutput = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/GetPathInfo.ashx'
        
class ListFolderReq(SessionTokenReq):
    """
    Nirvanix List Folder Request
    """
    folderPath = request.CharVariable(required=True)
    pageNumber = request.CharVariable(required=True)
    pageSize = request.CharVariable(required=True)
    sortCode = request.CharVariable()
    sortDescending = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/ListFolder.ashx'
        
class MoveFilesReq(SessionTokenReq):
    """
    Nirvanix Move Files Request
    """
    srcFilePath = request.CharVariable(required=True) 
    destFolderPath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/MoveFiles.ashx'
        
class MoveFoldersReq(SessionTokenReq):
    """
    Nirvanix Move Folders Request
    """
    srcFolderPath = request.CharVariable(required=True)
    destFolderPath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/MoveFolders.ashx'
     
class RenameFileReq(SessionTokenReq):
    """
    Nirvanix Rename File Request
    """
    filePath = request.CharVariable(required=True)
    newFileName = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/RenameFile.ashx'

class RenameFolderReq(SessionTokenReq):
    """
    Nirvanix Rename Folder Request
    """
    folderPath = request.CharVariable(required=True)
    newFolderName = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/RenameFolder.ashx'
        
class GetDownloadNodesReq(SessionTokenReq):
    """
    Nirvanix Get Download Nodes Request
    """
    filePath = request.CharVariable(required=True)
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/GetDownloadNodes.ashx'
        
class GetOptimalUrlsReq(SessionTokenReq):
    """
    Nirvanix Get Optimal URLs Request
    """
    filePath = request.CharVariable(required=True)
    expiration = request.CharVariable(required=True)
    consumerIP = request.CharVariable()
    ipRestricted = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/GetOptimalUrls.ashx'
        
class GetStorageNodeExtendedReq(SessionTokenReq):
    """
    Nirvanix Get Storage Node Extended Request
    """
    sizeBytes = request.CharVariable(required=True)
    destFolderPath = request.CharVariable(required=True)
    consumerIP = request.CharVariable()
    ipRestricted = request.CharVariable()
    fileOverwrite = request.CharVariable()
    firstByteExpiration = request.CharVariable()
    lastByteExpiration = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/GetStorageNodeExtended.ashx'
        
class GetStorageNodeReq(SessionTokenReq):
    """
    Nirvanix Get Storage Node Request
    """
    sizeBytes = request.CharVariable(required=True)
    restrictedIP = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/GetStorageNode.ashx'
        
class SearchFileSystemReq(SessionTokenReq):
    """
    Nirvanix Search File System Request
    """
    username = request.CharVariable(required=True)
    searchTerm = request.CharVariable(required=True)
    minFileSize = request.CharVariable(required=True)
    maxFileSize = request.CharVariable(required=True)
    minCreatedDate = request.CharVariable(required=True)
    maxCreatedDate = request.CharVariable(required=True)
    maxResults = request.CharVariable(required=True)
    fileType = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/SearchFileSystem.ashx'
        
class SideloadReq(SessionTokenReq):
    """
    Nirvanix Side Load Request
    """
    targetURL = request.CharVariable(required=True)
    destFilePath = request.CharVariable(required=True)
    callbackURL = request.CharVariable(required=True)
    fileOverwrite = request.CharVariable()
    
    class Meta(SessionTokenReq.Meta):
        request_path = 'ws/IMFS/Sideload.ashx'
        
