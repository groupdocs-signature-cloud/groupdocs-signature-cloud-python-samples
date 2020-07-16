# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class DeleteQRCode:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
                 
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedQRCodeOne_page.docx"

        # Search
        opts = SearchQRCodeOptions()        
        opts.page = 1
        opts.signature_type = 'QRCode'
        
        settings = SearchSettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = SearchSignaturesRequest(settings)
        response = api.search_signatures(request)
        
        # Delete
        opts = DeleteOptions()        
        opts.page = 1
        opts.signature_type = 'QRCode'
        opts.signature_id = response.signatures[0].signature_id
        
        settings = DeleteSettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = DeleteSignaturesRequest(settings)
        response = api.delete_signatures(request)

        print("Succeeded count: " + str(len(response.succeeded)))
