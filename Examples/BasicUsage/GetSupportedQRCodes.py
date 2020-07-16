# Import modules
import groupdocs_signature_cloud

from Common import Common

class GetSupportedQRCodes:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.InfoApi.from_config(Common.GetConfig())
        result = api.get_supported_qr_codes()
        print("QRCode types count: " + str(len(result.qr_code_types)))
