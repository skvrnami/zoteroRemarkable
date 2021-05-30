# Zotero Remarkable Sync

This is a little utility that I made to keep a collection/folder in sync with Zotero and reMarkable.
So far, it works only one way - upload papers from Zotero to reMarkable.

## Setup
- Install requirements
`pip install -r requirements.txt`
- Create `config.py` with the following content:
```
LIBRARY_ID = "XXXXX" # Zotero Library ID
API_KEY = "XXXXX" # Zotero API key
STORAGE_BASE_PATH = "/Users/{user}/Zotero/storage" # Path to local storage of Zotero
```

Library ID and Zotero API key is available at [https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys).

## Usage

Then to sync, just run:  
> `python3 sync.py -z {zotero_collection_name} -r {remarkable_folder_name}`

e.g.
> `python3 sync.py -z preferential-voting -r papers`
