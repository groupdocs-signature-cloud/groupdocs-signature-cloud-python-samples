# Import modules
import groupdocs_signature_cloud

from Common import Common

class CopyFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.CopyFileRequest("signaturedocs\\one-page.docx", "signaturedocs\\one-page-copied.docx", Common.myStorage, Common.myStorage)
            api.copy_file(request)
            
            print("Expected response type is Void: 'signaturedocs/one-page.docx' file copied as 'signaturedocs/one-page-copied.docx'.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))