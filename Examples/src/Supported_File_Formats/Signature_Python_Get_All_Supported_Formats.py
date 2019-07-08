# Import modules
import groupdocs_signature_cloud

from Common_Utilities.Utils import Common_Utilities;


class Signature_Python_Get_All_Supported_Formats:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_InfoApi_Instance()
        
        try:
            # Retrieve supported file-formats
            response = api.get_supported_file_formats()
    
            # Print out supported file-formats
            print("Supported file-formats:")
            for fileformat in response.formats:
                print('{0} ({1})'.format(fileformat.file_format, fileformat.extension))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception when calling get_supported_signature_types: {0}".format(e.message))