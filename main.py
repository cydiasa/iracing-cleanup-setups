"""
iRacing-Cleanup-Setups
After installing new vehicle setups in iRacing, I accidentally downloaded other things into my
vehicles folder. This script goes to the given path and removes anything that is not `-Current-`
or has an `.sto` extension
"""

import os
import argparse
from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dryrun',
    default=True,
    action='store_true',
    help="True by default. Pass in false to delete files"
)
parser.add_argument(
    '--dry-run',
    default=True,
    action=argparse.BooleanOptionalAction
)
args = parser.parse_args()
root_path = os.getenv("IRACING_INSTALL_PATH")

print("Script Start")
if args.dry_run is True:
    print("Dry run -- Files will not be deleted")

for folders in os.listdir(path=root_path):
    sub_folder_path = root_path + "\\" + folders
    for files in os.listdir(path=sub_folder_path):
        file_path = sub_folder_path + "\\" + files
        if files.lower() != "-current-" and not files.lower().endswith(".sto"):
            if not os.path.isdir(file_path):
                print("Found: " + file_path)
                if not args.dry_run:
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        print("Deleting: " + file_path)
                        os.remove(file_path)

print("Script Complete")
