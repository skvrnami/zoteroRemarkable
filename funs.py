def getCollectionId(zotero, collection_name):
    collections = zotero.collections(limit=200)
    for collection in collections:
        if (collection.get('data').get('name') == collection_name):
            return collection.get('data').get('key')

def getPapersTitleAndPathsFromZoteroCollection(zotero, collection_id, STORAGE_BASE_PATH):
    papers = []
    collection_items = zotero.collection_items(collection_id)
    for item in collection_items:
        if(item.get('data').get('contentType') == 'application/pdf') and item.get('data').get('linkMode') == 'imported_file':
            item_pdf_path = STORAGE_BASE_PATH + "/" + item.get('data').get('key') + "/" + item.get('data').get('filename')
            item_title = item.get('data').get('title')[:-4]
            if (item_pdf_path and item_title):
                papers.append({ 'title': item_title, 'path': item_pdf_path })
    return papers

def getPapersFromRemarkable(meta_items, folder_name):
    upload_folder = [ i for i in meta_items if i.VissibleName == folder_name ][0]

    return([ i.VissibleName for i in meta_items.children(upload_folder) if i.Type == "DocumentType" ])


def getUploadListOfPapers(remarkable_files, papers):
    upload_list = []
    for paper in papers:
        title = paper.get('title')
        # print(title)
        if title not in remarkable_files:
            upload_list.append(paper)
    return upload_list

"""
def getPapersFromRemarkable(RMAPI_LS):
    remarkable_files = []
    
    for f in subprocess.check_output(RMAPI_LS, shell=True).decode("utf-8").split('\n')[1:-1]:
        if '[d]\t' not in f:
            remarkable_files.append(f.strip('[f]\t'))
    return remarkable_files


def uploadPapers(papers):
    print(f'uploading {len(papers)} papers')
    for paper in papers:
        path = paper.get('path')
        COMMAND = f"{RMAPI} put \"{path}\" /{FOLDER_NAME}"
        try:
            print(COMMAND)
            os.system(COMMAND)
        except:
            print(f'Failed to upload {path}')

def getDeleteListOfPapers(remarkable_files, papers):
    delete_list = []
    paperNames = _(papers).map(lambda p: p.get('title')).value()
    for f in remarkable_files:
        if (f not in paperNames):
            delete_list.append(f)
    return delete_list

def deletePapers(delete_list):
    print(f'deleting {len(delete_list)} papers')
    for paper in delete_list:
        COMMAND = f"{RMAPI} rm /{FOLDER_NAME}/\"{paper}\""
        try:
            print(COMMAND)
            os.system(COMMAND)
        except:
            print(f'Failed to delete {paper}')
"""
