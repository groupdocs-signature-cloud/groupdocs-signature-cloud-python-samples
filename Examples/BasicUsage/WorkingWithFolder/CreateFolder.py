# Import modules
import groupdocs_signature_cloud

from Common import Common

class CreateFolder:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.CreateFolderRequest("Assembler", Common.myStorage)
            api.create_folder(request)
            
            print("Expected response type is Void: 'Assembler' folder created.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))