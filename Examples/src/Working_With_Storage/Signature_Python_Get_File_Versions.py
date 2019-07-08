# Import modules
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Get_File_Versions:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_StorageApi_Instance()
        
        try:
            request = groupdocs_signature_cloud.GetFileVersionsRequest("signaturedocs\\one-page.docx", Common_Utilities.myStorage)
            response = api.get_file_versions(request)
            
            print("Expected response type is FileVersions: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))