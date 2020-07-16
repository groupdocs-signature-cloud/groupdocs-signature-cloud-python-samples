# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class UpdateQRCode:    
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
        
        # Update
        opts = UpdateOptions()        
        opts.page = 1
        opts.signature_type = 'QRCode'
        opts.signature_id = response.signatures[0].signature_id
        opts.left = 200
        opts.top = 200
        opts.width = 200
        opts.height = 200
        opts.is_signature = True
        
        settings = UpdateSettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = UpdateSignaturesRequest(settings)
        response = api.update_signatures(request)

        print("Succeeded count: " + str(len(response.succeeded)))
