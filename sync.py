import argparse

from pyzotero import zotero as pyzotero
from pydash import _
from rmapy.api import Client
from rmapy.document import Document, ZipDocument

from config import API_KEY, LIBRARY_ID, STORAGE_BASE_PATH
from funs import getCollectionId, getPapersTitleAndPathsFromZoteroCollection, getPapersFromRemarkable, getUploadListOfPapers

parser = argparse.ArgumentParser(description='Sync reMarkable with Zotero.')
parser.add_argument('-z', help='Zotero collection to be synced', required=True)
parser.add_argument('-r', help='reMarkable folder to upload files', required=True)

args = parser.parse_args()

COLLECTION_NAME = args.z
FOLDER_NAME = args.r
LIBRARY_TYPE = 'user'

rm = Client()
rm.is_auth()
# rm.register_device("bupjirmx")
rm.renew_token()
rm.is_auth()

zotero = pyzotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)

print('------- sync started -------')
collection_id = getCollectionId(zotero, COLLECTION_NAME)

# get papers that we want from Zetero Remarkable collection
papers = getPapersTitleAndPathsFromZoteroCollection(zotero, collection_id, STORAGE_BASE_PATH)
print(f"{len(papers)} papers in Zotero {COLLECTION_NAME} collection name")
meta_items = rm.get_meta_items()

print('------- remarkable papers -------')
remarkable_papers = getPapersFromRemarkable(meta_items, FOLDER_NAME)

print('------- upload papers -------')
upload_papers = getUploadListOfPapers(remarkable_papers, papers)
upload_folder = [ i for i in meta_items if i.VissibleName == FOLDER_NAME ][0]

for i in upload_papers:
    print('Uploading: ' +  i.get('title'))
    upload_paper = i.get('path')
    rawDocument = ZipDocument(doc=upload_paper)
    rm.upload(rawDocument, upload_folder)
print('------- sync complete -------')

"""

#get papers that are currently on remarkable
remarkable_files = getPapersFromRemarkable(RMAPI_LS)
print(f"{len(remarkable_files)} papers on Remarkable Device, /{FOLDER_NAME}")

upload_list = getUploadListOfPapers(remarkable_files, papers)
uploadPapers(upload_list)

delete_list = getDeleteListOfPapers(remarkable_files, papers)
deletePapers(delete_list)
""" 
