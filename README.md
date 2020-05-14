# google_api_helper - Automate your google drive process easily
Detailed usage documentation is still in progress
The objective of this package is to help python developper to use some of the Google Drive API v3 easily.
As of now, 5 functions are available. This package is embedding very nicely with Google API libraries.

This is how you can install it on your machine:

```
pip install google_api_helper
```

All of the functionnalities of google_api_helper require you to build the the service class using google ServiceAccountCredentials.
For instance, you can use the ServiceAccountCredentials from json keyfile name as such:

```
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service():
    scopes = ['https://www.googleapis.com/auth/drive'
              , 'https://www.googleapis.com/auth/drive.file']
    
    key_file_location = 'pathtokeyfile.json'

    creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes=scopes)

    service = build('drive', 'v3', credentials=creds)
    print('connection OK')
    return service

service = get_service()

```

Once set, you can use our library and get, for instance, the folder tree of a specific file as such:

```
fileId = 'XXXXXXXXXXX' #id of the file you wish to get the folder tree for.
tree = find_fileid_tree(service, fileId)
```

## List of the functions available [last update: 5/14/2020]:

### get_google_folder_id(service, folder_name)
Get folder id of a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see www.pypi.com for a full example.
    folder_name: name of the folder you wish to get the ID of.

### get_google_folders_in_folder(service, folder_id)
Get a list of folders in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see www.pypi.com for a full example.
    folder_id: id of the folder you wish to get the folders list of.

### get_google_files_in_folder(service, folder_id)
Get a list of files and folders in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see www.pypi.com for a full example.
    folder_id: id of the folder you wish to get the folders list of.

### uplaod_google_file(service, MediaFileUpload, parent_id, file_name)
Upload a file in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see www.pypi.com for a full example.
    MediaFileUpload: function of oauth2client.service_account. see www.pypi.com for a full example.
    parent_id: id of the folder you wish to get the folders list of.
    file_name: local path to the file. If the file is in the same folder as your script, then you should only enter here the name of your file.

### find_google_fileid_tree(service, fileId)
Find the folder tree of a file

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see www.pypi.com for a full example.
    fileId: id of the file you wish to get the tree for.
