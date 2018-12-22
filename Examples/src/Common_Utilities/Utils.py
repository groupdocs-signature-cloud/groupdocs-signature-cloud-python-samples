# Import module
from groupdocs_signature_cloud.rest import ApiException
import groupdocs_signature_cloud
import asposestoragecloud
import json

class Common_Utilities:
    
    app_sid = ""
    app_key = ""
    storage_name = ""
    host = "http://api.groupdocs.cloud"   # Put your Host URL here
    base_url = "http://api.groupdocs.cloud/v1" #Put your Base URL here

    @staticmethod
    def Set_Globals(app_sidin, app_keyin, storage_namein, hostin, base_urlin):
        Common_Utilities.app_sid = app_sidin
        Common_Utilities.app_key = app_keyin
        Common_Utilities.host = hostin
        Common_Utilities.base_url = base_urlin
        Common_Utilities.storage_name = storage_namein
   
    @staticmethod
    def Get_SignatureApi_Instance():
        # initialization of configuration for signature api client
        configuration = groupdocs_signature_cloud.Configuration()
        configuration.host = Common_Utilities.host
        configuration.base_url = Common_Utilities.base_url
        configuration.api_key["api_key"] = Common_Utilities.app_key
        configuration.api_key["app_sid"] = Common_Utilities.app_sid

        # Create instance of the API
        return groupdocs_signature_cloud.SignatureApi(configuration=configuration)

    @staticmethod
    def Upload_Test_Files():
        
        try:
            print("Uploading test Files...")
            # initialization of configuration for storage api client
            storageConfiguration = asposestoragecloud.Configuration()
            storageConfiguration.host = Common_Utilities.host
            storageConfiguration.base_url = Common_Utilities.base_url
            storageConfiguration.api_key_prefix = "Bearer"
            configuration = groupdocs_signature_cloud.Configuration()
            configuration.api_key["api_key"] = Common_Utilities.app_key
            configuration.api_key["app_sid"] = Common_Utilities.app_sid
            resource_Folder = "Resources"
            
            # initialization of storage api client
            storageApiClient = asposestoragecloud.ApiClient(apiKey=str(configuration.api_key["api_key"]), appSid=str(configuration.api_key["app_sid"]), configuration=storageConfiguration)
            storageApi = asposestoragecloud.StorageApi(storageApiClient)
            
            from os import listdir
            from os.path import isfile, join
            onlyfiles = [f for f in listdir(resource_Folder) if isfile(join(resource_Folder, f))]
            
            for curFile in onlyfiles:
                # skip existing file uploading
                fileExistsResponse = storageApi.get_is_exist(curFile, storage = Common_Utilities.storage_name, _preload_content=False)
                responseData = json.loads(fileExistsResponse.data)
                
                if responseData["code"] == 200 and responseData["fileExist"]["isExist"] == False:
                    # file stream uploading
                    filestream = open(file = resource_Folder + "/" + curFile, mode = "rb")
                    storageApi.put_create(path = curFile, file = filestream, storage = Common_Utilities.storage_name)      
                    filestream.close()    
                    print("Uploaded: " + curFile)     
        except ApiException as e:
            print("Exception when calling SignatureApi: {0}".format(e.message))