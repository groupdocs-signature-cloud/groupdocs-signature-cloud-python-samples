# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class VerifyQRCode:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedQRCodeOne_page.docx"

        opts = VerifyQRCodeOptions()
        opts.signature_type = 'QRCode'
        opts.text = 'GroupDocs.Signature Cloud'
        opts.qr_code_type = 'Aztec'
        opts.match_type = 'Contains'
        
        opts.page = 1
        
        settings = VerifySettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = VerifySignaturesRequest(settings)
        response = api.verify_signatures(request)
            
        print("IsSuccess: " + str(response.is_success))
