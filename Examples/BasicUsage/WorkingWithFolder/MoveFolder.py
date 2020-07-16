# Import modules
import groupdocs_signature_cloud

from Common import Common

class MoveFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.MoveFolderRequest("signaturedocs1", "signaturedocs1\\signaturedocs", Common.myStorage, Common.myStorage)
            api.move_folder(request)
            
            print("Expected response type is Void: 'signaturedocs1' folder moved to 'signaturedocs/signaturedocs1'.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))