# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Search_Digital_Signature:
    
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
    
            opts = SearchDigitalOptions()        
            opts.document_type = "WordProcessing"
            # set signature properties
            opts.signature_type = 'Digital'
            opts.match_type = 'Contains'
            opts.left = 100
            opts.top = 100
            opts.width = 200
            opts.height = 100
            opts.location_measure_type = "Pixels"
            opts.size_measure_type = "Pixels"        
            opts.rotation_angle = 0
            opts.horizontal_alignment = "None"
            opts.vertical_alignment = "None"
            opts.margin = Padding()
            opts.margin.all = 5
            opts.margin_measure_type = "Pixels"
            
            settings = SearchSettings()
            settings.options = [opts]
            settings.file_info = fileInfo
    
            request = SearchSignaturesRequest(settings)
            response = api.search_signatures(request)
            
            print("Signatures length: " + str(len(response.signatures)))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Search_Digital_Signature: {0}".format(e.message))