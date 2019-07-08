# Import modules
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Copy_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_signature_cloud.CopyFolderRequest("signaturedocs", "signaturedocs1", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_folder(request)
            
            print("Expected response type is Void: 'signaturedocs' folder copied as 'signaturedocs1'.")
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))