# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class StampSignature:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.SignApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\one-page.docx"

        opts = SignStampOptions()        
        opts.signature_type = 'Stamp'
        opts.image_file_path = "signaturedocs\\signature.jpg"
        
        # set signature position on a page
        opts.left = 100
        opts.top = 100
        opts.width = 300
        opts.height = 200
        opts.location_measure_type = "Pixels"
        opts.size_measure_type = "Pixels"        
        opts.rotation_angle = 0
        opts.horizontal_alignment = "None"
        opts.vertical_alignment = "None"
        opts.margin = Padding()
        opts.margin.all = 5
        opts.margin_measure_type = "Pixels"
        
        # set signature appearance
        opts.background_color = Color()
        opts.background_color.web = "CornflowerBlue"   
        opts.background_color_crop_type = "InnerArea"
        opts.background_image_crop_type = "MiddleArea"
        
        outline = StampLine()
        outline.text = "John Smith"
        outline.font = SignatureFont()
        outline.font.font_family = "Arial"
        outline.font.font_size = 12
        outline.font.bold = True
        outline.font.italic = True
        outline.font.underline = True
        outline.text_bottom_intent = 5
        outline.text_color = Color()
        outline.text_color.web = "Gold"
        outline.text_repeat_type = "FullTextRepeat"
        outline.background_color = Color()
        outline.background_color.web = "BlueViolet"
        outline.height = 20
        outline.inner_border = BorderLine()
        outline.inner_border.color = Color()
        outline.inner_border.color.web = "DarkOrange"
        outline.inner_border.style = "LongDash"
        outline.inner_border.transparency = 0.5
        outline.inner_border.weight = 1.2
        outline.outer_border = BorderLine()
        outline.outer_border.color = Color()
        outline.outer_border.color.web = "DarkOrange"
        outline.outer_border.style = "LongDashDot"
        outline.outer_border.transparency = 0.7
        outline.outer_border.weight = 1.4        
        outline.visible = True
        opts.outer_lines = [outline]
        
        innerline = StampLine()
        innerline.text = "John Smith"
        innerline.font = SignatureFont()
        innerline.font.font_family = "Times New Roman"
        innerline.font.font_size = 20
        innerline.font.bold = True
        innerline.font.italic = True
        innerline.font.underline = True
        innerline.text_bottom_intent = 3
        innerline.text_color = Color()
        innerline.text_color.web = "Gold"
        innerline.text_repeat_type = "None"
        innerline.background_color = Color()
        innerline.background_color.web = "CornflowerBlue"
        innerline.height = 30
        innerline.inner_border = BorderLine()
        innerline.inner_border.color = Color()
        innerline.inner_border.color.web = "OliveDrab"
        innerline.inner_border.style = "LongDash"
        innerline.inner_border.transparency = 0.5
        innerline.inner_border.weight = 1.2
        innerline.outer_border = BorderLine()
        innerline.outer_border.color = Color()
        innerline.outer_border.color.web = "GhostWhite"
        innerline.outer_border.style = "Dot"
        innerline.outer_border.transparency = 0.4
        innerline.outer_border.weight = 1.4        
        innerline.visible = True
        opts.inner_lines = [innerline]
        
        opts.page = 1
        
        settings = SignSettings()
        settings.options = [opts]
        
        settings.save_options = SaveOptions()
        settings.save_options.output_file_path = "signaturedocs\\signedStampOne_page.docx"
        settings.file_info = fileInfo

        request = CreateSignaturesRequest(settings)
        response = api.create_signatures(request)
        
        print("Succeeded count: " + str(len(response.succeeded)))
