from restxl.client import RestXLer
from auth_requests import *
from download_requests import *
from billing_mgmt_requests import *
from file_requests import *
from log_search_requests import *
from metadata_requests import *
from o_auth_requests import *
from replication_policy_requests import *
from replication_requests import *
from upload_requests import *
from user_info_requests import *

class Diomede(RestXLer):
    def __init__(self,
                 username=None,
                 password=None,
                 session_token=None):
        self.username = username
        self.password = password

        if session_token:
            self.session_token = session_token
        else:
            tt = self.login()
            self.session_token = getattr(tt.content.sessionToken, '_',None)
            
    def login(self):
        cs = LoginReq(
            username=self.username,
            password=self.password,
            )
        tt = cs()
        self.session_token = tt.content.sessionToken._
        return tt
        
    create_user = CreateUserReq
    delete_user = DeleteUserReq
    change_password = ChangePasswordReq
    reset_password = ResetPasswordReq
    logout = LogoutReq
    
    #Billing Managment requests
    get_all_products = GetAllProductsReq
    get_my_products = GetMyProductsReq
    purchase_product = PurchaseProductReq
    cancel_product = CancelProductReq
    get_all_contracts = GetAllContractsReq
    purchase_contract = PurchaseContractReq
    cancel_contract = CancelContractReq
    
    #Download requests
    get_download_url = GetDownloadURLReq
    download = DownloadReq
    
    #File requests
    search_files = SearchFilesReq
    search_files_total = SearchFilesTotalReq
    delete_file = DeleteFileReq
    rename_or_delete = RenameOrDeleteFileReq
    
    #Log Search requests
    search_login_log = SearchLoginLogReq
    search_invoice_log = SearchInvoiceLogReq
    search_payment_log = SearchPaymentLogReq
    search_files_total_log = SearchFilesTotalLogReq
    search_download_log = SearchDownloadLogReq
    search_upload_log = SearchUploadLogReq
    
    #Metadata Requests
    create_metadata = CreateMetaDataReq
    get_file_metadata = GetFileMetaDataReq
    set_file_metadata = SetFileMetadataReq
    delete_file_metadata = DeleteFileMetadataReq
    create_metadata = CreateMetaDataReq
    get_metadata = GetMetaDataReq
    edit_metadata = EditMetaDataReq
    delete_metadata = DeleteMetaDataReq
    
    #O Auth Requests
    create_o_auth = CreateOAuthReq
    get_o_auth_secret_key = GetOAuthSecretKeyReq
    
    #Replication Policy requests
    create_replication_policy = CreateRepPolicyReq
    get_replication_policy = GetRepPoliciesReq
    edit_replication_policy = EditRepPolicyReq
    delete_replication_policy = DeleteRepPolicyReq
    set_default_replication_policy = SetDefaultRepPolicyReq
    get_default_replication_policy = GetDefaultRepPolicyReq
    set_replication_policy = SetRepPolicyReq
    
    #Replication Requests
    replicate_file = ReplicateFileReq
    unreplicate_file = UnReplicateFileReq
    get_physical_file = GetPhysicalFileReq
    get_storage_types = GetStorageTypesReq
    
    #Upload Requests
    create_file = CreateFileReq
    upload_file = UploadFileReq
    
    #User Info requests
    set_user_info = SetUserInfoReq
    delete_user_info = DeleteUserInfoReq
    get_email_address = GetEmailAddressReq
    add_email_address = AddEmailAddressReq
    delete_email_address = DeleteEmailAddressReq
    set_prime_email = SetPrimeEmailReq
    