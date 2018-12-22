# Import module
from groupdocs_signature_cloud.rest import ApiException
from Common_Utilities.Utils import Common_Utilities

class File_Formats:

    @staticmethod
    def Get_All_Supported_File_Formats():
        
        try:
            # Getting instance of the API
            api = Common_Utilities.Get_SignatureApi_Instance();

            # Retrieve supported file-formats
            response = api.get_supported_formats(True)
            
            # Print out supported file-formats
            print("Supported file-formats:")
            for formatval in response.formats:
                print('{0} ({1})'.format(formatval.file_format, formatval.extension)) 
        except ApiException as e:
            print("Exception when calling SignatureApi: {0}".format(e.message))