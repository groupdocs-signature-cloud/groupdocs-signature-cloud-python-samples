# Import modules
import groupdocs_signature_cloud

from Common import Common

class MoveFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.MoveFileRequest("signaturedocs\\one-page.docx", "signaturedocs1\\one-page.docx", Common.myStorage, Common.myStorage)
            api.move_file(request)
            
            print("Expected response type is Void: 'signaturedocs/one-page.docx' file moved to 'signaturedocs1/one-page.docx'.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))