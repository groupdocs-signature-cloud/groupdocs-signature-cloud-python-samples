# Import modules
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities


class Signature_Python_Get_Disc_Usage:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_StorageApi_Instance()
        
        try:
            request = groupdocs_signature_cloud.GetDiscUsageRequest(Common_Utilities.myStorage)
            response = api.get_disc_usage(request)
            
            print("Expected response type is DiscUsage: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))