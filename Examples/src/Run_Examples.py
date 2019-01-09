# Import module
from Common_Utilities.Utils import Common_Utilities
from Supported_File_Formats.Signature_Python_Supported_FileFormats import File_Formats
from Document_Information.Signature_Python_DocumentInfo_File import DocumentInfo_File
from Document_Information.Signature_Python_DocumentInfo_URL import DocumentInfo_From_Url
from Supported_Barcodes.Signature_Python_Supported_Barcodes import Supported_Barcodes
from Supported_QRCodes.Signature_Python_Supported_QRcodes import Supported_QRcodes
from Signing_Documents.Working_with_Barcode_Signature.Signature_Python_Signature_Barcode import Signature_Barcode
from Signing_Documents.Working_with_Barcode_Signature.Signature_Python_Signature_Barcode_From_URL import Signature_Barcode_From_Url
from Signing_Documents.Working_with_Digital_Signature.Signature_Python_Signature_Digital import Signature_Digital
from Signing_Documents.Working_with_Digital_Signature.Signature_Python_Signature_Digital_URL import Signature_Digital_From_Url
from Signing_Documents.Working_with_Image_Signature.Signature_Python_Signature_Image import Signature_Image
from Signing_Documents.Working_with_Image_Signature.Signature_Python_Signature_Image_URL import Signature_Image_From_Url
from Signing_Documents.Working_with_QR_Code_Signature.Signature_Python_Signature_QRCode import Signature_QRCode
from Signing_Documents.Working_with_QR_Code_Signature.Signature_Python_Signature_QRCode_URL import Signature_QRCode_From_Url
from Signing_Documents.Working_with_QR_Code_Signature.Signature_Python_Signature_QRCode_Logo_Image import Signature_QRCode_Logo
from Signing_Documents.Working_with_Signature_Collection.Signature_Python_Signature_Collection import Signature_Collection
from Signing_Documents.Working_with_Signature_Collection.Signature_Python_Signature_Collection_FromUrl import Signature_Collection_From_Url
from Signing_Documents.Working_with_Stamp_Signature.Signature_Python_Signature_Stamp import Signature_Stamp
from Signing_Documents.Working_with_Stamp_Signature.Signature_Python_Signature_Stamp_URL import Signature_Stamp_From_Url
from Signing_Documents.Working_with_Stamp_Signature.Signature_Python_Signature_Stamp_Background_Brush import Signature_Stamp_Background_Brush
from Signing_Documents.Working_with_Text_Signature.Signature_Python_Signature_Text import Signature_Text
from Signing_Documents.Working_with_Text_Signature.Signature_Python_Signature_Text_URL import Signature_Text_From_Url
from Signing_Documents.Working_with_Text_Signature.Signature_Python_Signature_Text_Background_Brush import Signature_Text_Background_Brush
from Verifying_Signature.Verify_Barcode_Signature.Signature_Python_Verify_Signature_Barcode import Verify_Signature_Barcode
from Verifying_Signature.Verify_Barcode_Signature.Signature_Python_Verify_Signature_Barcode_URL import Verify_Signature_Barcode_From_Url
from Verifying_Signature.Verify_Digital_Signature.Signature_Python_Verify_Signature_Digital import Verify_Signature_Digital
from Verifying_Signature.Verify_Digital_Signature.Signature_Python_Verify_Signature_Digital_URL import Verify_Signature_Digital_From_Url
from Verifying_Signature.Verify_QRCode_Signature.Signature_Python_Verify_Signature_QRCode import Verify_Signature_QRCode
from Verifying_Signature.Verify_QRCode_Signature.Signature_Python_Verify_Signature_QRCode_URL import Verify_Signature_QRCode_From_Url
from Verifying_Signature.Verify_Text_Signature.Signature_Python_Verify_Signature_Text import Verify_Signature_Text
from Verifying_Signature.Verify_Text_Signature.Signature_Python_Verify_Signature_Text_URL import Verify_Signature_Text_From_Url
from Verifying_Signature.Working_with_Verify_Collection.Signature_Python_Signature_Collection_Verify import Verify_Signature_Collection
from Verifying_Signature.Working_with_Verify_Collection.Signature_Python_Signature_Collection_Verify_FromUrl import Verify_Signature_Collection_From_Url
from Search_Signature.Search_Barcode_Signature.Signature_Python_Search_Signature_Barcode import Search_Signature_Barcode
from Search_Signature.Search_Barcode_Signature.Signature_Python_Search_Signature_Barcode_URL import Search_Signature_Barcode_From_Url
from Search_Signature.Search_Digital_Signature.Signature_Python_Search_Signature_Digital import Search_Signature_Digital
from Search_Signature.Search_Digital_Signature.Signature_Python_Search_Signature_Digital_URL import Search_Signature_Digital_From_Url
from Search_Signature.Search_QRCode_Signature.Signature_Python_Search_Signature_QRCode import Search_Signature_QRCode
from Search_Signature.Search_QRCode_Signature.Signature_Python_Search_Signature_QRCode_URL import Search_Signature_QRCode_From_Url
from Search_Signature.Working_with_Search_Collection.Signature_Python_Search_Collection import Search_Collection
from Search_Signature.Working_with_Search_Collection.Signature_Python_Search_Collection_FromUrl import Search_Collection_From_Url

class Run_Examples:

    # Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
    app_sid = "XXXXXXX"
    app_key = "XXXXX-XXX"
    storageName = "MyStorage" #Put your storage name here
    host = "http://api.groupdocs.cloud"   # Put your Host URL here
    base_url = "http://api.groupdocs.cloud/v1" #Put your Base URL here
    Common_Utilities.Set_Globals(app_sid, app_key, storageName, host, base_url);
    
    # Upload Test files
    Common_Utilities.Upload_Test_Files()
      
    # ******* Execute Examples *******
    print("*** Executing examples...")
    # ******* Execute Examples *******
      
    print("* Executing Get_All_Supported_File_Formats...")
    File_Formats.Get_All_Supported_File_Formats()
      
    print("* Executing Get_DocumentInfo_File...")
    DocumentInfo_File.Get_DocumentInfo_File()
      
    print("* Executing Get_DocumentInfo_From_Url...")
    DocumentInfo_From_Url.Get_DocumentInfo_From_Url()
  
    print("* Executing Get_All_Supported_Barcodes...")
    Supported_Barcodes.Get_All_Supported_Barcodes()
  
    print("* Executing Get_All_Supported_QRcodes...")
    Supported_QRcodes.Get_All_Supported_QRcodes()
  
    print("* Executing Post_Signature_Barcode...")
    #Signature_Barcode.Post_Signature_Barcode()
  
    print("* Executing Post_Signature_Barcode_From_Url...")
    Signature_Barcode_From_Url.Post_Signature_Barcode_From_Url()
  
    print("* Executing Post_Signature_Digital...")
    #Signature_Digital.Post_Signature_Digital()
  
    print("* Executing Post_Signature_Digital_From_Url...")
    Signature_Digital_From_Url.Post_Signature_Digital_From_Url()
 
    print("* Executing Post_Signature_Image...")
    #Signature_Image.Post_Signature_Image()
  
    print("* Executing Post_Signature_Image_From_Url...")
    Signature_Image_From_Url.Post_Signature_Image_From_Url()
   
    print("* Executing Post_Signature_QRCode...")
    #Signature_QRCode.Post_Signature_QRCode()
  
    print("* Executing Post_Signature_QRCode_From_Url...")
    Signature_QRCode_From_Url.Post_Signature_QRCode_From_Url()
  
    print("* Executing Post_Signature_QRCode_Logo...")
    #Signature_QRCode_Logo.Post_Signature_QRCode_Logo()
  
    print("* Executing Post_Signature_Collection...")
    #Signature_Collection.Post_Signature_Collection()
   
    print("* Executing Post_Signature_Collection_From_Url...")
    #Signature_Collection_From_Url.Post_Signature_Collection_From_Url()
  
    print("* Executing Post_Signature_Stamp...")
    #Signature_Stamp.Post_Signature_Stamp()
  
    print("* Executing Post_Signature_Stamp_From_Url...")
    Signature_Stamp_From_Url.Post_Signature_Stamp_From_Url()
  
    print("* Executing Post_Signature_Stamp_Background_Brush...")
    Signature_Stamp_Background_Brush.Post_Signature_Stamp_Background_Brush()
  
    print("* Executing Post_Signature_Text...")
    #Signature_Text.Post_Signature_Text()
      
    print("* Executing Post_Signature_Text_From_Url...")
    Signature_Text_From_Url.Post_Signature_Text_From_Url()
  
    print("* Executing Post_Signature_Text_Background_Brush...")
    #Signature_Text_Background_Brush.Post_Signature_Text_Background_Brush()
 
    print("* Executing Post_Verify_Signature_Barcode...")
    Verify_Signature_Barcode.Post_Verify_Signature_Barcode()
 
    print("* Executing Post_Verify_Signature_Barcode_From_Url...")
    Verify_Signature_Barcode_From_Url.Post_Verify_Signature_Barcode_From_Url()
  
    print("* Executing Post_Verify_Signature_Digital...")
    Verify_Signature_Digital.Post_Verify_Signature_Digital()
  
    print("* Executing Post_Verify_Signature_Digital_From_Url...")
    Verify_Signature_Digital_From_Url.Post_Verify_Signature_Digital_From_Url()
   
    print("* Executing Post_Verify_Signature_QRCode...")
    Verify_Signature_QRCode.Post_Verify_Signature_QRCode()
   
    print("* Executing Post_Verify_Signature_QRCode_From_Url...")
    Verify_Signature_QRCode_From_Url.Post_Verify_Signature_QRCode_From_Url()
   
    print("* Executing Post_Verify_Signature_Text...")
    Verify_Signature_Text.Post_Verify_Signature_Text()
 
    print("* Executing Post_Verify_Signature_Text_From_Url...")
    Verify_Signature_Text_From_Url.Post_Verify_Signature_Text_From_Url()
   
    print("* Executing Post_Verify_Signature_Collection...")
    Verify_Signature_Collection.Post_Verify_Signature_Collection()
  
    print("* Executing Post_Verify_Signature_Collection_From_Url...")
    Verify_Signature_Collection_From_Url.Post_Verify_Signature_Collection_From_Url()
  
    print("* Executing Post_Search_Signature_Barcode...")
    Search_Signature_Barcode.Post_Search_Signature_Barcode()
  
    print("* Executing Post_Search_Signature_Barcode_From_Url...")
    Search_Signature_Barcode_From_Url.Post_Search_Signature_Barcode_From_Url()
  
    print("* Executing Post_Search_Signature_Digital...")
    Search_Signature_Digital.Post_Search_Signature_Digital()
  
    print("* Executing Post_Search_Signature_Digital_From_Url...")
    Search_Signature_Digital_From_Url.Post_Search_Signature_Digital_From_Url()
  
    print("* Executing Post_Search_Signature_QRCode...")
    Search_Signature_QRCode.Post_Search_Signature_QRCode()
  
    print("* Executing Post_Search_Signature_QRCode_From_Url...")
    Search_Signature_QRCode_From_Url.Post_Search_Signature_QRCode_From_Url()
  
    print("* Executing Post_Search_Collection...")
    Search_Collection.Post_Search_Collection()
  
    print("* Executing Post_Search_Collection_From_Url...")
    Search_Collection_From_Url.Post_Search_Collection_From_Url()
    print("Execution completed!")
