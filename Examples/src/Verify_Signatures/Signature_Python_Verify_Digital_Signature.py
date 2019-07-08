# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Verify_Digital_Signature:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_SignApi_Instance()
        
        try:            
            fileInfo = FileInfo()
            fileInfo.file_path = "signaturedocs\\signedDigitalOne_page.docx"
            fileInfo.password = None
            fileInfo.version_id = None
            fileInfo.storage_name = Common_Utilities.myStorage
    
            opts = VerifyDigitalOptions()
            # set signature properties
            opts.document_type = "WordProcessing"
            opts.signature_type = 'Digital'
            opts.page = 1
            opts.all_pages = True
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            opts.pages_setup = ps
            
            settings = VerifySettings()
            settings.options = [opts]
            settings.file_info = fileInfo
    
            request = VerifySignaturesRequest(settings)
            response = api.verify_signatures(request)
            
            print("Response File Info: " + str(response.file_info))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Verify_Digital_Signature: {0}".format(e.message))