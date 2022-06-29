# Import modules
from groupdocs_signature_cloud import *
import groupdocs_signature_cloud

from Common import Common

# This example demonstrates how to get metered license consumption info
class GetLicenseConsumption:
    @classmethod  
    def Run(cls):
        licenseApi = groupdocs_signature_cloud.LicenseApi.from_config(Common.GetConfig())
        result = licenseApi.get_consumption_credit()
        print("Credits = " + str(result.credit))