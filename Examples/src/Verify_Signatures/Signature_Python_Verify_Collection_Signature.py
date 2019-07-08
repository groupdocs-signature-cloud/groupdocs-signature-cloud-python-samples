# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Verify_Collection_Signature:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_SignApi_Instance()
        
        try:            
            fileInfo = FileInfo()
            fileInfo.file_path = "signaturedocs\\signedCollectionOne_page.docx"
            fileInfo.password = None
            fileInfo.version_id = None
            fileInfo.storage_name = Common_Utilities.myStorage
    
            Barcodeopts = VerifyBarcodeOptions()
            # set signature properties
            Barcodeopts.document_type = "WordProcessing"
            Barcodeopts.signature_type = 'Barcode'
            Barcodeopts.text = '123456789012'
            Barcodeopts.barcode_type = 'Code39Standard'
            Barcodeopts.match_type = 'Contains'
            
            Barcodeopts.page = 1
            Barcodeopts.all_pages = True
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            Barcodeopts.pages_setup = ps
            
            QRCodeopts = VerifyQRCodeOptions()
            # set signature properties
            QRCodeopts.document_type = "WordProcessing"
            QRCodeopts.signature_type = 'QRCode'
            QRCodeopts.text = 'GroupDocs.Signature Cloud'
            QRCodeopts.qr_code_type = 'Aztec'
            QRCodeopts.match_type = 'Contains'
            
            QRCodeopts.page = 1
            QRCodeopts.all_pages = True
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            QRCodeopts.pages_setup = ps
            
            settings = VerifySettings()
            settings.options = [Barcodeopts,QRCodeopts]
            settings.file_info = fileInfo
    
            request = VerifySignaturesRequest(settings)
            response = api.verify_signatures(request)
            
            print("Response File Info: " + str(response.file_info))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Verify_Collection_Signature: {0}".format(e.message))