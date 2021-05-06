# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

class GetDocumentPreview:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.PreviewApi.from_config(Common.GetConfig())
        
        fileInfo = FileInfo()
        fileInfo.file_path = "signaturedocs\\one-page.docx"
        fileInfo.password = None
        fileInfo.version_id = None
        fileInfo.storage_name = Common.myStorage

        settings = PreviewSettings()
        settings.file_info = fileInfo

        request = PreviewDocumentRequest(settings)
        response = api.preview_document(request)
        
        print("Page count = " + str(len(response.pages)))
