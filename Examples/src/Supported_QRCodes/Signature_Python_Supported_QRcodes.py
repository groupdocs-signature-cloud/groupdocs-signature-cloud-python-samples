# Import module
from groupdocs_signature_cloud.rest import ApiException
from Common_Utilities.Utils import Common_Utilities
from groupdocs_signature_cloud.models.requests.get_qr_codes_request import GetQrCodesRequest
class Supported_QRcodes:

	@staticmethod
	def Get_All_Supported_QRcodes():

		try:
			# Getting instance of the API
			api = Common_Utilities.Get_SignatureApi_Instance();
			
			request = GetQrCodesRequest()
			
			response = api.get_qr_codes(request)
			for curItem in response.qr_code_types:
				print(curItem.name)

		except ApiException as e:
			print("Exception when calling SignatureApi: {0}".format(e.message))
