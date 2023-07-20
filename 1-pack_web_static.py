from fabric.api import run
from datetime import datetime
import tarfile
import os
import glob

# get current date
current_date = datetime.now().strftime("%Y%m%d%H%M%S")

# set filenames
dump_file = "/web_static/*"
archive_file = f"versions/web_static_{current_date}.tgz"


def do_pack():
    # Create new directory if not present
    new_directory = "versions"
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    # Get files list using glob
    files = glob.glob(dump_file)

    # Create compressed archive
    with tarfile.open(archive_file, "w:gz") as tar:
        for file in files:
            print(f"Packing {file}")
            tar.add(file, arcname=os.path.basename(file))

    # Get the size of the archive file
    archive_size = os.path.getsize(archive_file)

    print(f"web_static packed: {archive_file} -> {archive_size} bytes")
    print("\nDone.")
