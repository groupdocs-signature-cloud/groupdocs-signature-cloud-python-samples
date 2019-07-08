# Import modules
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities;


class Signature_Python_Get_Supported_QRCodes:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_InfoApi_Instance()
        
        try:
            # Retrieve supported file-formats
            response = api.get_supported_qr_codes()
    
            # Print out supported file-formats
            print("Supported barcode_types:")
            for fileformat in response.qr_code_types:
                print('{0})'.format(fileformat.name ))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling Signature_Python_Get_Supported_QRCodes: {0}".format(e.message))