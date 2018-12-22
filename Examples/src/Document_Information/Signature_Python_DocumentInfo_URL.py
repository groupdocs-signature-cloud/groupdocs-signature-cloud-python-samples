# Import module
from groupdocs_signature_cloud.rest import ApiException
from Common_Utilities.Utils import Common_Utilities
from groupdocs_signature_cloud.models.requests.get_document_info_from_url_request import GetDocumentInfoFromUrlRequest

class DocumentInfo_From_Url:

	@staticmethod
	def Get_DocumentInfo_From_Url():

		try:
			# Getting instance of the API
			api = Common_Utilities.Get_SignatureApi_Instance();

			url = "https://www.dropbox.com/s/bzx1xm68zd0c910/PieChart.docx?dl=0"
			password = ""

			request = GetDocumentInfoFromUrlRequest(url, password, Common_Utilities.storage_name)

			response = api.get_document_info_from_url(request)

			print("FleName: " + str(response.name));
			print("Folder: " + str(response.folder));

		except ApiException as e:
			print("Exception when calling SignatureApi: {0}".format(e.message))