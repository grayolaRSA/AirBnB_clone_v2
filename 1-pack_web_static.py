#!/usr/bin/python3
"""
Fabric script to create tar archive of web static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create "versions" directory if not present"""
    new_directory = "versions"
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    # Get the current date and time in the desired format
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")

    # Generate the archive filename
    archive_file = f"{new_directory}/web_static_{current_date}.tgz"

    # Create the compressed archive using the "tar" command
    command = local("tar -czvf {} web_static".format(archive_file))
    result = local(command)

    # Check if the archive has been correctly generated
    if result.succeeded:
        # Get the size of the archive file
        archive_size = os.path.getsize(archive_file)

        print(f"web_static packed: {archive_file} -> {archive_size} bytes")
        return archive_file
    else:
        return None
