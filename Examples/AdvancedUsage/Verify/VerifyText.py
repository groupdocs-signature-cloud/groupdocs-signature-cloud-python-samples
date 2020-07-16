# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class VerifyText:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedTextOne_page.docx"

        opts = VerifyTextOptions()
        opts.signature_type = 'Text'
        opts.text = 'GroupDocs.Signature Cloud'
        opts.match_type = 'Contains'
        
        opts.page = 1
        
        settings = VerifySettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = VerifySignaturesRequest(settings)
        response = api.verify_signatures(request)
        
        print("IsSuccess: " + str(response.is_success))
