# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Search_QRCode_Signature:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_SignApi_Instance()
        
        try:            
            fileInfo = FileInfo()
            fileInfo.file_path = "signaturedocs\\signedQRCodeOne_page.docx"
            fileInfo.password = None
            fileInfo.version_id = None
            fileInfo.storage_name = Common_Utilities.myStorage
    
            opts = SearchBarcodeOptions()        
            opts.document_type = "WordProcessing"
            # set signature properties
            opts.page = 1
            opts.all_pages = True
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            opts.pages_setup = ps
            opts.signature_type = 'QRCode'
            opts.match_type = 'Contains'
            
            settings = SearchSettings()
            settings.options = [opts]
            settings.file_info = fileInfo
    
            request = SearchSignaturesRequest(settings)
            response = api.search_signatures(request)
            
            print("Signatures length: " + str(len(response.signatures)))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Search_QRCode_Signature: {0}".format(e.message))