# Import modules
import groupdocs_signature_cloud

from Common import Common

class UploadFile:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FileApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.UploadFileRequest("signaturedocs\\one-page.docx", "D:\\ewspace\\GroupDocs.Signature.Cloud.Python.Examples\\src\\Resources\\signaturedocs\\one-page.docx", Common.myStorage)
            response = api.upload_file(request)
            
            print("Expected response type is FilesUploadResult: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))