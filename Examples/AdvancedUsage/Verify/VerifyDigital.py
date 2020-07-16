# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class VerifyDigital:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedDigitalOne_page.docx"

        opts = VerifyDigitalOptions()
        opts.signature_type = 'Digital'
        opts.page = 1
        opts.all_pages = True
        
        settings = VerifySettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = VerifySignaturesRequest(settings)
        response = api.verify_signatures(request)
        
        print("IsSuccess: " + str(response.is_success))
