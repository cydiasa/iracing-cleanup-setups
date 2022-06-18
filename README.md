# iRacing-Cleanup-Setups
After installing new vehicle setups in iRacing, I accidentally downloaded other things into my vehicles folder. This script goes to the given path and removes anything that is not `-Current-` or has an `.sto` extension

## Setup and Run
- pip install -r requirements.txt
    - install requirments
- python main.py
    - Run in dry-run mode. No files will be deleted.
- python main.py --no-dry-run
    - Files will be *deleted* when found.

## Warning
This script:
- Will delete files with extention `.sto`
- Will delete files with name of `-Current-`
- Will not delete folders
- Will not create backups
- Will not delete items in subfolders