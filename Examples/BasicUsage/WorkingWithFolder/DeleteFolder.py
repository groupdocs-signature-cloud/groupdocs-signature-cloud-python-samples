# Import modules
import groupdocs_signature_cloud

from Common import Common

class DeleteFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.DeleteFolderRequest("signaturedocs\\signaturedocs1", Common.myStorage, True)
            api.delete_folder(request)
            
            print("Expected response type is Void: 'signaturedocs/signaturedocs1' folder deleted recursively.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))