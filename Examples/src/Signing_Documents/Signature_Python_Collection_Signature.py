# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Collection_Signature:
    
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
    
            Barcodeopts = SignBarcodeOptions()        
            Barcodeopts.document_type = "WordProcessing"
            # set signature properties
            Barcodeopts.signature_type = 'Barcode'
            Barcodeopts.text = '123456789012'
            Barcodeopts.barcode_type = 'Code128'
            Barcodeopts.code_text_alignment = 'None'
            
            # set signature position on a page
            Barcodeopts.left = 100
            Barcodeopts.top = 100
            Barcodeopts.width = 300
            Barcodeopts.height = 100
            Barcodeopts.location_measure_type = "Pixels"
            Barcodeopts.size_measure_type = "Pixels"
            Barcodeopts.stretch = "None"
            Barcodeopts.rotation_angle = 0
            Barcodeopts.horizontal_alignment = "None"
            Barcodeopts.vertical_alignment = "None"
            Barcodeopts.margin = Padding()
            Barcodeopts.margin.all = 5
            Barcodeopts.margin_measure_type = "Pixels"
            
            # set signature appearance
            Barcodeopts.fore_color = Color()
            Barcodeopts.fore_color.web = "BlueViolet"
            Barcodeopts.border_color = Color()
            Barcodeopts.border_color.web = "DarkOrange"
            Barcodeopts.background_color = Color()
            Barcodeopts.background_color.web = "DarkOrange"
            Barcodeopts.opacity = 0.8
            Barcodeopts.inner_margins = Padding()
            Barcodeopts.inner_margins.all = 2
            Barcodeopts.border_visiblity = True
            Barcodeopts.border_dash_style = "Dash"
            Barcodeopts.border_weight = 12
            
            Barcodeopts.page = 1
            Barcodeopts.all_pages = False
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            Barcodeopts.pages_setup = ps
            
            QRCodeopts = SignQRCodeOptions()        
            QRCodeopts.document_type = "WordProcessing"
            # set signature properties
            QRCodeopts.signature_type = 'QRCode'
            QRCodeopts.text = 'GroupDocs.Signature Cloud'
            QRCodeopts.qr_code_type = 'Aztec'        
            
            # set signature position on a page
            QRCodeopts.left = 100
            QRCodeopts.top = 100
            QRCodeopts.width = 200
            QRCodeopts.height = 100
            QRCodeopts.location_measure_type = "Pixels"
            QRCodeopts.size_measure_type = "Pixels"
            QRCodeopts.stretch = "None"
            QRCodeopts.rotation_angle = 0
            QRCodeopts.horizontal_alignment = "None"
            QRCodeopts.vertical_alignment = "None"
            QRCodeopts.margin = Padding()
            QRCodeopts.margin.all = 5
            QRCodeopts.margin_measure_type = "Pixels"
            
            # set signature appearance
            QRCodeopts.fore_color = Color()
            QRCodeopts.fore_color.web = "BlueViolet"
            QRCodeopts.border_color = Color()
            QRCodeopts.border_color.web = "DarkOrange"
            QRCodeopts.background_color = Color()
            QRCodeopts.background_color.web = "DarkOrange"
            QRCodeopts.opacity = 0.8
            QRCodeopts.inner_margins = Padding()
            QRCodeopts.inner_margins.all = 2
            QRCodeopts.border_visiblity = True
            QRCodeopts.border_dash_style = "Dash"
            QRCodeopts.border_weight = 12
            
            QRCodeopts.page = 1
            QRCodeopts.all_pages = False
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            QRCodeopts.pages_setup = ps
            
            settings = SignSettings()
            settings.options = [Barcodeopts,QRCodeopts]
            
            settings.save_options = SaveOptions()
            settings.save_options.output_file_path = "signaturedocs\\signedCollectionOne_page.docx"
            settings.file_info = fileInfo
    
            request = CreateSignaturesRequest(settings)
            response = api.create_signatures(request)
            
            print("file_path: " + response.file_info.file_path)
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Collection_Signature: {0}".format(e.message))