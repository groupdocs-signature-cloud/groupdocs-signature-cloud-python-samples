# Import modules
import os
import groupdocs_signature_cloud
from Common import Common

# Get your ClientId and ClientSecret at https://dashboard.groupdocs.cloud (free registration is required).
Common.client_id = "XXXX-XXXX-XXXX-XXXX"
Common.client_secret = "XXXXXXXXXXXXXXXX"

Common.myStorage = "First Storage"

# Uploading sample test files from local disk to cloud storage
Common.UploadSampleFiles()

# BasicUsage examples

from BasicUsage.GetSupportedFormats import GetSupportedFormats
GetSupportedFormats.Run()
from BasicUsage.GetSupportedBarcodes import GetSupportedBarcodes
GetSupportedBarcodes.Run()
# from BasicUsage.GetSupportedQRCodes import GetSupportedQRCodes
# GetSupportedQRCodes.Run()
from BasicUsage.GetDocumentInfo import GetDocumentInfo
GetDocumentInfo.Run()

# AdvancedUsage examples

from AdvancedUsage.Sign.BarcodeSignature import BarcodeSignature
BarcodeSignature.Run()
# from AdvancedUsage.Sign.BarcodeSignature import BarcodeSignature
# BarcodeSignature.Run()
# from AdvancedUsage.Sign.CollectionSignature import CollectionSignature
# CollectionSignature.Run()
# from AdvancedUsage.Sign.DigitalSignature import DigitalSignature
# DigitalSignature.Run()
# from AdvancedUsage.Sign.ImageSignature import ImageSignature
# ImageSignature.Run()
# from AdvancedUsage.Sign.QRCodeSignature import QRCodeSignature
# QRCodeSignature.Run()
# from AdvancedUsage.Sign.StampSignature import StampSignature
# StampSignature.Run()
# from AdvancedUsage.Sign.TextSignature import TextSignature
# TextSignature.Run()

from AdvancedUsage.Search.SearchBarcode import SearchBarcode
SearchBarcode.Run()
# from AdvancedUsage.Search.SearchCollection import SearchCollection
# SearchCollection.Run()
# from AdvancedUsage.Search.SearchDigital import SearchDigital
# SearchDigital.Run()
# from AdvancedUsage.Search.SearchQRCode import SearchQRCode
# SearchQRCode.Run()

from AdvancedUsage.Verify.VerifyBarcode import VerifyBarcode
VerifyBarcode.Run()
# from AdvancedUsage.Verify.VerifyCollection import VerifyCollection
# VerifyCollection.Run()
# from AdvancedUsage.Verify.VerifyDigital import VerifyDigital
# VerifyDigital.Run()
# from AdvancedUsage.Verify.VerifyQRCode import VerifyQRCode
# VerifyQRCode.Run()
# from AdvancedUsage.Verify.VerifyText import VerifyText
# VerifyText.Run()

from AdvancedUsage.Update.UpdateBarcode import UpdateBarcode
UpdateBarcode.Run()
# from AdvancedUsage.Update.UpdateQRCode import UpdateQRCode
# UpdateQRCode.Run()

from AdvancedUsage.Delete.DeleteBarcode import DeleteBarcode
DeleteBarcode.Run()
# from AdvancedUsage.Delete.DeleteQRCode import DeleteQRCode
# DeleteQRCode.Run()
