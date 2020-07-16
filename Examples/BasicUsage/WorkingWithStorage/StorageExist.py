# Import modules
import groupdocs_signature_cloud

from Common import Common

class StorageExist:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.StorageApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.StorageExistsRequest(Common.myStorage)
            response = api.storage_exists(request)
            
            print("Expected response type is StorageExist: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))