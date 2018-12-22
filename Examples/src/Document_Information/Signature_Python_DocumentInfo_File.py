# Import module
from groupdocs_signature_cloud.rest import ApiException
from Common_Utilities.Utils import Common_Utilities
from groupdocs_signature_cloud.models.requests.get_document_info_request import GetDocumentInfoRequest

class DocumentInfo_File:

	@staticmethod
	def Get_DocumentInfo_File():

		try:
			# Getting instance of the API
			api = Common_Utilities.Get_SignatureApi_Instance();

			fileName = "one-page.docx"
			password = ""
			folder = ""

			request = GetDocumentInfoRequest(fileName, password, folder, Common_Utilities.storage_name)

			response = api.get_document_info(request)

			print("FleName: " + str(response.name));
			print("Folder: " + str(response.folder));

		except ApiException as e:
			print("Exception when calling SignatureApi: {0}".format(e.message))