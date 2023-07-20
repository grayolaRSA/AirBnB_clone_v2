#!/usr/bin/python3
"""
Fabric script to run various server functions
"""

from fabric.api import local, put, run, env
from datetime import datetime
import os
import glob
env.hosts = ['100.25.12.227', '34.224.63.152']


def do_pack():
    """Create new tar archive of static files"""
    new_directory = "versions"
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)

    # Get the current date and time in the desired format
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")

    # Generate the archive filename
    archive_file = f"{new_directory}/web_static_{current_date}.tgz"

    # Create the compressed archive using the "tar" command
    command = local(
        f"tar -czvf {archive_file} web_static")
    result = local(command)

    # Check if the archive has been correctly generated
    if result.succeeded:
        # Get the size of the archive file
        archive_size = os.path.getsize(archive_file)

        print(f"web_static packed: {archive_file} -> {archive_size} bytes")
        return archive_file
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
