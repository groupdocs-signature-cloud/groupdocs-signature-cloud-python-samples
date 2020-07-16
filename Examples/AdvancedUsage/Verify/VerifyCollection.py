# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class VerifyCollection:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\signedCollectionOne_page.docx"

        Barcodeopts = VerifyBarcodeOptions()
        Barcodeopts.signature_type = 'Barcode'
        Barcodeopts.text = '123456789012'
        Barcodeopts.barcode_type = 'Code39Standard'
        Barcodeopts.match_type = 'Contains'
        
        Barcodeopts.page = 1
        
        QRCodeopts = VerifyQRCodeOptions()
        QRCodeopts.signature_type = 'QRCode'
        QRCodeopts.text = 'GroupDocs.Signature Cloud'
        QRCodeopts.qr_code_type = 'Aztec'
        QRCodeopts.match_type = 'Contains'
        
        QRCodeopts.page = 1
        
        settings = VerifySettings()
        settings.options = [Barcodeopts,QRCodeopts]
        settings.file_info = fileInfo

        request = VerifySignaturesRequest(settings)
        response = api.verify_signatures(request)
        
        print("IsSuccess: " + str(response.is_success))
