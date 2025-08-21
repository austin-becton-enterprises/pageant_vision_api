# Pageant Vision API

## Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create your environment files (`.env.staging`, `.env.prod`). You can copy `.env.staging` to get started and fill in your production secrets in `.env.prod`.

4. Run the API:

For staging environment (with auto-reload):
```bash
APP_ENV=staging uvicorn main:app --reload
```

For production environment:
```bash
APP_ENV=prod uvicorn main:app
```

The API will be available at http://localhost:8000

API Documentation available at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Environment Configuration

The API supports different environments through `.env` files:
- `.env.prod` - Production settings
- `.env.staging` - Staging settings with debug mode enabled

Environment variables can be overridden by setting them before running the application:
```bash
export APP_ENV=staging
export DEBUG=true
```




 
    /*
    @StateObject private var videoViewModel = VideoPlayerViewModel(videoURL: URL(string: "https://stream.mux.com/tUm5VcWUYQjOBsHO00vOgIj02ljpv302p7kXU001JUpCnE4.m3u8?token=")!)
    """
    key id 41ff10eb-2a4f-4ca0-948b-697b1ec5db57
    secret key w5TnN96zs2bplyEbzvT4HEvOpN0hX6TyfRfn5koaYi/cc8bmCAdydaJjFNS37mKbaYMD91iLAkC
    """
     
     """
     signing key:
     ID:
     
     
     Private Key (base64)
     cueDygoBG2kDCnh9mhzGIjhtFRVecVMowr7FZ4yGeI00


     
     
     LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcEFJQkFBS0NBUUVBMDFwemh2UEdaSUs1cmd2Qmg3a01TQkJ1VHBzZWNDOXhYaFNSZVVrNGhKaE1QaGpiCml4SC9rY2psd21kVzRENVJYRHBJQ3hHa3VkTDBnNGV2TW9CMUdaL2U1T0J4Vm1tUTVYR1crcHcvUU5qcWVEUnoKcnMxYnpXdzVOcWozWlRKelVCV0VnbnVJNFRuQ0FYdVRNeERqY0FtZmFPK3hhRFdpSFVmOWhLS3ZJSlR2cEFBcQpmQkFUNE9mVTNTYktEUTQ5QkNNUENhQTE3VlBlMU1YYnZKT1Nrb1E0SnN4clBkWXBHU2pyZHJaS2wvNnlESHJaCkYyUFNMNUxETGxtOG9MS3IyV0FNVXhONFZrbU1CcWh0aWd6ajM1R3JPdmNNbXFPZ01NWVFTMmtRZzVCTGxid3cKMU9NeHRoZk9qVlYxR01mSEZUNDBaTFVBaW1RQmdibHJCOE1YSndJREFRQUJBb0lCQUFGUGRwYzlSd1h6MkRUZgp0blBNbzVVd0lqbWQzKzF3SXpMTnk5ZkZxc2UxQTF3QWlYUHVTUGhkYk5kQ0RzUXJLV2xQVHpKZnRLRnJwbXB6CnIrbGtsSC96MXN6eWUwd1VNWHJLczlYdjhXWEozU3oyU1BWVTAvU05HWThMaUhwNXorODNndS9RSzVsc2plc0wKeE1PSjlPOEtrRHQxVTZpWUZJam1tN0xKS01Ra21yS2d5SnlQZGJ1cXRJYTl2NFN0RWlhYzlwMm5WQkU1NjltcQpwcExiYzZkOFkyVERNYkNpQ01pSUoxUDQraittSzhkbEd5QlIvYXl3MWJWVGFjdUZNZkdtN2hiV3NlamlZS0V4CjdaYUI0bkd2TzdKeVdyWEpadjhFUFdxdnppMGsybkxHNXR5U05DdS9lK2ZmakNPOXhJdlBqTEg0Y1lPT1IxME0KREFMVFk5RUNnWUVBOTFaOStqN1E5ck1zUDAvTjFyMzZZZHFIamVlT0hxNGdpT0VZLzBQZjR4d3VQSnpRa2VrcAowdjRMdm9qbTRqWWw0YUtLMUVkbGE3dnNNL1IvbUlQY0xXSHFNd1BaN2VDOFpkT2U1cWJYUUp1R2h6c3NpOER6CmgycHNCQm9pazJCazdYSHd6Y1JWMEVmalNqVEZVdEwzRnVjL3Z2UU1WT0FyMHpBSXZ0aW1teGtDZ1lFQTJzRlcKL0Z4SVlTUTNYZ25yWDJmb1NKRGNDdTRHRmc2eUlldGhHMTBzdjNaUElOTlRqcTFDcG1SeVVTNU0ybkVmaHZseQpHd1BLdmM1RFpPbkRMSTRKM1JFT1JJODBCM2dadmF5eldhdmp3K0RwdUF2d2FvQW5UdWNzbjNSV2lTUEgzdVhVCjJ1UXpCNVBOMU1PWGVkL1BQMEEwVW5ZSUlROWRNWGxWU0V6anpEOENnWUJUb2R0WEVvWjE1SC9CcUtwaFFqdTMKZXJ6N0xxRFBudkZCVjF1c2RMYnZoRWZlRnVndmJqZkdNRUNvWElJMVd6blQ0Ykl2dFRTR0NUVUZIRmRJcXMxNApTdk4xN0lkejk5bThWS0lXTzdQdEZLbVljRm5QcDU2dzJ6dEs1OHRwS2Q3MnF1QlJzMkdRMjczdkNZanZTSVprCktDMVYxQStYWTNWdUkzL1JpRkJOZ1FLQmdRQ3dFU1QrQVJpUWR5SEpJcHE3TTFxVjdXSHR1aDVUNm9nZEhPSVAKc0RLdjkzMUFvbGFDWTVsZGEwTkhhOGlYbUswVGFmb1pIRGcyQktuaHN2UlFEQktNUjRvQVRISklBTFpYSDRWTApDenBMRWQrTExyRFdSMGRjRGx5d0NtY01BaXlBanVOL09tU0lHTUoyR09iMlJOajl3Nk5aSzM3bmZRSTVLN3NrCmNoNTI2UUtCZ1FETkk0M251VEkyaENzbVZmQmRBeER3TXZ4WHM3ZHZnVDNlcTFIK2VCdmI5UFVid0JKYjlVeVQKVnNUVkNUdVZzcWZ1S2grZ0pDYTNrNnNUVmRQRHN1aXdJOHZxVlJqbFNjTHEwRmxtT2hnWTBFYS9Vdy96SWNrVgpQLzhwbE93UkI3UGNhMjdjZk5ZanlScHphd3h2cDVyUTA5MzlpcUZPb0JuRC9RYURHVm9KaWc9PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo=
     """
    */

    /*
    Validation failed
Missing required icon file. The bundle does not contain an app icon for iPhone / iPod Touch of exactly '120x120' pixels, in .png format for iOS versions >= 10.0. To support older versions of iOS, the icon may be required in the bundle outside of an asset catalog. Make sure the Info.plist file includes appropriate entries referencing the file. See https://developer.apple.com/documentation/bundleresources/information_property_list/user_interface. (ID: 0ec72cff-8617-47d5-93a1-6110c47d8396)

Validation failed
Missing required icon file. The bundle does not contain an app icon for iPad of exactly '152x152' pixels, in .png format for iOS versions >= 10.0. To support older operating systems, the icon may be required in the bundle outside of an asset catalog. Make sure the Info.plist file includes appropriate entries referencing the file. See https://developer.apple.com/documentation/bundleresources/information_property_list/user_interface. (ID: ca46190b-02ee-45a9-938d-03b5eebb7125)

Validation failed
Missing Info.plist value. A value for the Info.plist key 'CFBundleIconName' is missing in the bundle 'Becton-Enterprises.PageantVision'. Apps built with iOS 11 or later SDK must supply app icons in an asset catalog and must also provide a value for this Info.plist key. For more information see http://help.apple.com/xcode/mac/current/#/dev10510b1f7. (ID: 15c1cb35-afcf-4a48-893e-4a8ac30245f3)

Upload Symbols Failed
The archive did not include a dSYM for the MuxCore.framework with the UUIDs [2296FDF1-D374-3FA6-AD2A-E4C70E9A7B7B]. Ensure that the archive's dSYM folder includes a DWARF file for MuxCore.framework with the expected UUIDs.
    */
    