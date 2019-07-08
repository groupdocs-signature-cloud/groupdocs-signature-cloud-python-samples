# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Barcode_Signature:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_SignApi_Instance()
        
        try:            
            fileInfo = FileInfo()
            fileInfo.file_path = "signaturedocs\\one-page.docx"
            fileInfo.password = None
            fileInfo.version_id = None
            fileInfo.storage_name = Common_Utilities.myStorage
    
            opts = SignBarcodeOptions()        
            opts.document_type = "WordProcessing"
            # set signature properties
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
            
            # set signature appearance
            opts.fore_color = Color()
            opts.fore_color.web = "BlueViolet"
            opts.border_color = Color()
            opts.border_color.web = "DarkOrange"
            opts.background_color = Color()
            opts.background_color.web = "DarkOrange"
            opts.opacity = 0.8
            opts.inner_margins = Padding()
            opts.inner_margins.all = 2
            opts.border_visiblity = True
            opts.border_dash_style = "Dash"
            opts.border_weight = 12
            
            opts.page = 1
            opts.all_pages = False
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            opts.pages_setup = ps
            
            settings = SignSettings()
            settings.options = [opts]
            settings.save_options = SaveOptions()
            settings.save_options.output_file_path = "signaturedocs\\signedBarcodeOne_page.docx"
            settings.file_info = fileInfo
    
            request = CreateSignaturesRequest(settings)
            response = api.create_signatures(request)
            
            print("file_path: " + response.file_info.file_path)
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Barcode_Signature: {0}".format(e.message))