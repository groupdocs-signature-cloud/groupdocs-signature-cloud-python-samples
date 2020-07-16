# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class GetDocumentInfo:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.InfoApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\one-page.docx"
        fileInfo.password = None
        fileInfo.version_id = None
        fileInfo.storage_name = Common.myStorage

        settings = InfoSettings()
        settings.file_info = fileInfo

        request = GetInfoRequest(settings)
        response = api.get_info(request)
        
        print("Page count = " + str(response.pages_count))