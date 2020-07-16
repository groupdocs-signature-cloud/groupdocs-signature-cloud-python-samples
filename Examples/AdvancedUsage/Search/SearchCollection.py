# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class SearchCollection:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedCollectionOne_page.docx"

        Digitalopts = SearchDigitalOptions()        
        Digitalopts.signature_type = 'Digital'
        
        Barcodeopts = SearchBarcodeOptions()        
        Barcodeopts.page = 1
        Barcodeopts.signature_type = 'Barcode'
        
        settings = SearchSettings()
        settings.options = [Digitalopts,Barcodeopts]
        settings.file_info = fileInfo

        request = SearchSignaturesRequest(settings)
        response = api.search_signatures(request)
        
        print("Signatures length: " + str(len(response.signatures)))
