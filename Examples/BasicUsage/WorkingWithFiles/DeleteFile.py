# Import modules
import groupdocs_signature_cloud

from Common import Common

class DeleteFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.DeleteFileRequest("signaturedocs1\\one-page.docx", Common.myStorage)
            api.delete_file(request)
            
            print("Expected response type is Void: 'signaturedocs1/one-page.docx' deleted.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))