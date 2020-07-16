# Import modules
import groupdocs_signature_cloud

from Common import Common

class GetFileVersions:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.GetFileVersionsRequest("signaturedocs\\one-page.docx", Common.myStorage)
            response = api.get_file_versions(request)
            
            print("Expected response type is FileVersions: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))