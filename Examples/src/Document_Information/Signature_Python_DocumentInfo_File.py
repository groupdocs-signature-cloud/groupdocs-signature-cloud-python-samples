# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_DocumentInfo_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_InfoApi_Instance()
        
        try:            
            fileInfo = FileInfo()
            fileInfo.file_path = "Signaturedocs\\one-page.docx"
            fileInfo.password = None
            fileInfo.version_id = None
            fileInfo.storage_name = Common_Utilities.myStorage
    
            settings = InfoSettings()
            settings.file_info = fileInfo
    
            request = GetInfoRequest(settings)
            response = api.get_info(request)
            
            print("file_path: " + response.file_info.file_path)
        except ApiException as e:
            print("Exception when calling Signature_Python_DocumentInfo_File: {0}".format(e.message))