def get_google_folder_id(service, folder_name):
  """Get folder id of a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see https://pypi.org/project/google-api-v3-helper/ or https://github.com/sbi-rviot/google_api_helper for a full example.
    folder_name: name of the folder you wish to get the ID of.

  """
  page_token = None
  while True:
    children = service.files().list(q="mimeType='application/vnd.google-apps.folder'", spaces='drive',fields='nextPageToken, files(id, name)').execute()
    for i in children['files']:
        if i['name'] == folder_name:
            folder_id = i['id']
            break
    page_token = children.get('nextPageToken', None)
    if page_token is None:
        break
  return folder_id


def get_google_folders_in_folder(service, folder_id):
  """Get a list of folders in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see https://pypi.org/project/google-api-v3-helper/ or https://github.com/sbi-rviot/google_api_helper for a full example.
    folder_id: id of the folder you wish to get the folders list of.

  """
  files_list = []
  page_token = None
  while True:
    children = service.files().list(q="mimeType='application/vnd.google-apps.folder' and parents='"+folder_id+"' and trashed=false",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)').execute()
    for file in children.get('files', []):
        files_list.append({'name':file.get('name'), 'id':file.get('id')})
    page_token = children.get('nextPageToken', None)
    if page_token is None:
        break
  return files_list


def get_google_files_in_folder(service, folder_id):
  """Get a list of files and folders in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see https://pypi.org/project/google-api-v3-helper/ or https://github.com/sbi-rviot/google_api_helper for a full example.
    folder_id: id of the folder you wish to get the folders list of.

  """
  files_list = []
  page_token = None
  while True:
    children = service.files().list(q="parents='"+folder_id+"' and trashed=false",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)').execute()
    for file in children.get('files', []):
        files_list.append({'name':file.get('name'), 'id':file.get('id')})
    page_token = children.get('nextPageToken', None)
    if page_token is None:
        break
  return files_list


def uplaod_google_file(service, MediaFileUpload, parent_id, file_name):
  """Upload a file in a folder in Google Drive

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see https://pypi.org/project/google-api-v3-helper/ or https://github.com/sbi-rviot/google_api_helper for a full example.
    MediaFileUpload: function of oauth2client.service_account. see www.pypi.com for a full example.
    parent_id: id of the folder you wish to get the folders list of.
    file_name: local path to the file. If the file is in the same folder as your script, then you should only enter here the name of your file.
  """
  file_metadata = {
                  'parents' : [parent_id],
                  'name': file_name}
  media = MediaFileUpload(file_name)
  file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
  return parent_id


def find_google_fileid_tree(service, fileId):
  """Find the folder tree of a file

  Arguments:
    service: in order to use any of this library, the user needs to first build the service class using google ServiceAccountCredentials. see https://pypi.org/project/google-api-v3-helper/ or https://github.com/sbi-rviot/google_api_helper for a full example.
    fileId: id of the file you wish to get the tree for.
  """
  file = service.files().get(fileId=fileId, fields='id, name, parents').execute()
  tree = []
  parent = file.get('parents')
  if parent:
      while True:
          folder = service.files().get(
              fileId=parent[0], fields='id, name, parents').execute()
          parent = folder.get('parents')
          if parent is None:
              break
          tree.append({'id': parent[0], 'name': folder.get('name')})

  return tree