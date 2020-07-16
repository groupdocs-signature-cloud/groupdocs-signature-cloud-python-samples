# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class TextSignature:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\one-page.docx"

        opts = SignTextOptions()        
        opts.signature_type = 'Text'
        opts.text = 'GroupDocs.Signature Cloud'
        
        # set signature position on a page
        opts.left = 100
        opts.top = 100
        opts.width = 100
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
        
        # set signature appearance
        opts.font = SignatureFont()
        opts.font.font_family = "Arial"
        opts.font.font_size = 12
        opts.font.bold = True
        opts.font.italic = False
        opts.font.underline = False        
        opts.fore_color = Color()
        opts.fore_color.web = "BlueViolet"
        opts.background_color = Color()
        opts.background_color.web = "DarkOrange"
        
        opts.page = 1
        
        settings = SignSettings()
        settings.options = [opts]
        settings.save_options = SaveOptions()
        settings.save_options.output_file_path = "signaturedocs\\signedTextOne_page.docx"
        settings.file_info = fileInfo

        request = CreateSignaturesRequest(settings)
        response = api.create_signatures(request)
        
        print("Succeeded count: " + str(len(response.succeeded)))
