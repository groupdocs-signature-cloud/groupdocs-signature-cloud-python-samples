# Import modules
import groupdocs_signature_cloud

from Common import Common

class CopyFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.CopyFolderRequest("signaturedocs", "signaturedocs1", Common.myStorage, Common.myStorage)
            api.copy_folder(request)
            
            print("Expected response type is Void: 'signaturedocs' folder copied as 'signaturedocs1'.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))