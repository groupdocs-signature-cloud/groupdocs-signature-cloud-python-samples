# Import modules
import groupdocs_signature_cloud

from Common import Common

class GetFilesList:    
    @classmethod
    def Run(cls):
        # Create instance of the API
        api = groupdocs_signature_cloud.FolderApi.from_config(Common.GetConfig())
        
        try:
            request = groupdocs_signature_cloud.GetFilesListRequest("signaturedocs\\sample.docx", Common.myStorage)
            response = api.get_files_list(request)
            
            print("Expected response type is FilesList: " + str(response))
        except groupdocs_signature_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))