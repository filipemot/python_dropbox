import dropbox


def upload_file(file_from, file_to):
    """
    Upload file from dropbox
    :param str | file_from:
        The path of input file
    :param str | file_to:
        The path of output file
    """
    try:
       dbx = dropbox.Dropbox('dropbox_acess_token')


        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    except:
        print('upload_file() - dropbox_service', 'Error')


def list_files(folder):
    """
    List folder's files in dropbox
    :param str | folder:
        The path of files
    """
    try:
        dbx = dropbox.Dropbox('dropbox_acess_token')
        return dbx.files_list_folder(path=folder)
    except:
       print('list_files() - dropbox_service', 'Error')


def share_link(file):
    """
    Get shared link of file
    :param str | file:
        The path of file
    """
    try:
       dbx = dropbox.Dropbox('dropbox_acess_token')
        try:
            shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file)
            return shared_link_metadata.url
        except:
            shared_link_metadata = dbx.sharing_list_shared_links(file)
            return shared_link_metadata.links[0].url
    except:
       print('share_link() - dropbox_service', 'Error')




def remove_file(file):
    """
    Remove File
    :param str | file:
        The path of file
    """
    try:
        dbx = dropbox.Dropbox('dropbox_acess_token')
        dbx.files_delete(file)
    except:
       print('remove_file() - dropbox_service', 'Error')