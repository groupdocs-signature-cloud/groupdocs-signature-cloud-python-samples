# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Search_Collection_Signature:
    
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
    
            Digitalopts = SearchDigitalOptions()        
            Digitalopts.document_type = "WordProcessing"
            # set signature properties
            Digitalopts.signature_type = 'Digital'
            Digitalopts.match_type = 'Contains'
            Digitalopts.left = 100
            Digitalopts.top = 100
            Digitalopts.width = 200
            Digitalopts.height = 100
            Digitalopts.location_measure_type = "Pixels"
            Digitalopts.size_measure_type = "Pixels"        
            Digitalopts.rotation_angle = 0
            Digitalopts.horizontal_alignment = "None"
            Digitalopts.vertical_alignment = "None"
            Digitalopts.margin = Padding()
            Digitalopts.margin.all = 5
            Digitalopts.margin_measure_type = "Pixels"
            
            Barcodeopts = SearchBarcodeOptions()        
            Barcodeopts.document_type = "WordProcessing"
            # set signature properties
            Barcodeopts.page = 1
            Barcodeopts.all_pages = True
            ps = PagesSetup()
            ps.even_pages = False
            ps.first_page = True
            ps.last_page = False
            ps.odd_pages = False
            ps.page_numbers = [1]
            Barcodeopts.pages_setup = ps
            Barcodeopts.signature_type = 'Barcode'
            Barcodeopts.barcode_type = 'Code39Standard'
            Barcodeopts.text = '123456789012'
            Barcodeopts.match_type = 'Contains'
            
            settings = SearchSettings()
            settings.options = [Digitalopts,Barcodeopts]
            settings.file_info = fileInfo
    
            request = SearchSignaturesRequest(settings)
            response = api.search_signatures(request)
            
            print("Signatures length: " + str(len(response.signatures)))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Search_Collection_Signature: {0}".format(e.message))