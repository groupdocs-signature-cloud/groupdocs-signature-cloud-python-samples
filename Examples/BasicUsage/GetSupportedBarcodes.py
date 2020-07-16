# Import modules
import groupdocs_signature_cloud

from Common import Common

class GetSupportedBarcodes:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.InfoApi.from_config(Common.GetConfig())
        result = api.get_supported_barcodes()
        print("Barcode types count: " + str(len(result.barcode_types)))
