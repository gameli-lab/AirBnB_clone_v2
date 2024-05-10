#!/usr/bin/python3
"""
Using fabric to compress files before uploading them to an my server
"""
from fabric import task
import os
from datetime import datetime


@task
def do_pack(c):
    """
    Compresses the 'web_static' directory into a tar archive and saves it in the 'versions' directory.
    
    This function uses the tar command to create a .tgz archive of the 'web_static'
    directory. The archive is named using a timestamp in the format:
    "web_static_YYYYMMDDHHMMSS.tgz".
    
    The function returns the path of the created archive if successful, None
    otherwise.
    
    Parameters:
        c (Connection): The connection object used to execute the command.
    """
    """ Create the 'versions' directory if it doesn't exist """
    if not os.path.exists('versions'):
        os.makedirs('versions')

    """ Create a timestamp in the format: YYYYMMDDHHMMSS """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    """ Create the archive name """
    arch_name = f"web_static_{timestamp}.tgz"

    """ Create the full path of the archive """
    arch_path = os.path.join("versions", arch_name)

    """ Change to the 'web_static' directory and execute the tar command """
    with c.cd('web_static'):
        res = c.run(f"tar -cvzf {arch_path} .")

    """ If the tar command fails, return None """
    if res.failed:
        return (None)

    """ Return the path of the created archive """
    return (arch_path)
