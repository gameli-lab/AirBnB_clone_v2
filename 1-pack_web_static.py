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

    """
    if not os.path.exists('versions'):
        os.makedirs('versions')

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    arch_name = f"web_static_{timestamp}.tgz"

    arch_path = os.path.join("versions", arch_name)

    with c.cd('web_static'):
        res = c.run(f"tar -cvzf {arch_path} .")

    if res.failed:
        return (None)

    return (arch_path)
