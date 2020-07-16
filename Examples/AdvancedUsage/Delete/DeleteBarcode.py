# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class DeleteBarcode:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
                 
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedBarcodeOne_page.docx"

        # Search
        opts = SearchBarcodeOptions()        
        opts.page = 1
        opts.signature_type = 'Barcode'
        
        settings = SearchSettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = SearchSignaturesRequest(settings)
        response = api.search_signatures(request)
        
        # Delete
        opts = DeleteOptions()        
        opts.page = 1
        opts.signature_type = 'Barcode'
        opts.signature_id = response.signatures[0].signature_id
        
        settings = DeleteSettings()
        settings.options = [opts]
        settings.file_info = fileInfo

        request = DeleteSignaturesRequest(settings)
        response = api.delete_signatures(request)

        print("Succeeded count: " + str(len(response.succeeded)))
