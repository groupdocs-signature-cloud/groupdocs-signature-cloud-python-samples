# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class BarcodeSignature:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\one-page.docx"

        opts = SignBarcodeOptions()        
        opts.signature_type = 'Barcode'
        opts.text = '123456789012'
        opts.barcode_type = 'Code128'
        opts.code_text_alignment = 'None'
        
        # set signature position on a page
        opts.left = 100
        opts.top = 100
        opts.width = 300
        opts.height = 100
        opts.location_measure_type = "Pixels"
        opts.size_measure_type = "Pixels"
        opts.stretch = "None"
        opts.rotation_angle = 0
        opts.horizontal_alignment = "None"
        opts.vertical_alignment = "None"
        opts.margin = Padding()
        opts.margin.all = 5
        opts.margin_measure_type = "Pixels"
        
        opts.inner_margins = Padding()
        opts.inner_margins.all = 2
        
        opts.page = 1
        
        settings = SignSettings()
        settings.options = [opts]
        settings.save_options = SaveOptions()
        settings.save_options.output_file_path = "signaturedocs\\signedBarcodeOne_page.docx"
        settings.file_info = fileInfo

        request = CreateSignaturesRequest(settings)
        response = api.create_signatures(request)
        
        print("Succeeded count: " + str(len(response.succeeded)))
