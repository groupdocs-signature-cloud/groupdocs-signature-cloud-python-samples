# Import modules
import groupdocs_signature_cloud

from Common import Common

class DownloadFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.DownloadFileRequest("signaturedocs\\one-page.docx", Common.myStorage)
            response = api.download_file(request)
            
            print("Expected response type is Stream: " + str(len(response)))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))