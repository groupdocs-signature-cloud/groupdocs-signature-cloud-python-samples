# Import module
from groupdocs_signature_cloud.rest import ApiException
from Common_Utilities.Utils import Common_Utilities
from groupdocs_signature_cloud.models.requests.get_barcodes_request import GetBarcodesRequest

class Supported_Barcodes:

	@staticmethod
	def Get_All_Supported_Barcodes():

		try:
			# Getting instance of the API
			api = Common_Utilities.Get_SignatureApi_Instance();
			
			request = GetBarcodesRequest()
			
			response = api.get_barcodes(request)
			for curItem in response.barcode_types:
				print(curItem.name)

		except ApiException as e:
			print("Exception when calling SignatureApi: {0}".format(e.message))
			