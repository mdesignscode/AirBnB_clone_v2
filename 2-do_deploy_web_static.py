#!/usr/bin/python3
"""distributes web servers using fabric"""

from fabric.operations import put, run, sudo
from fabric.api import env
from os.path import exists


env.hosts = ['44.210.15.126', '3.230.162.118']


def do_deploy(archive_path):
    """distributes web servers

    Args:
        archive_path (str): the path of archive
    """

    if not exists(archive_path):
        return False

    r1 = put(archive_path, '/tmp/')

    count = archive_path.count('/')
    name = archive_path.split('/')[count]
    no_ext = name.split('.')[0]
    rel = '/data/web_static/releases/'
    link = '/data/web_static/current'

    run(f'mkdir -p {rel}{no_ext}')

    r2 = run(f"tar -xzf /tmp/{name} -C {rel}{no_ext}")

    sudo(f"mv {rel}{no_ext}/web_static/* {rel}{no_ext}")

    r3 = run(f'rm -rf /tmp/{name} {link} {rel}{no_ext}/web_static/')

    r4 = run(f'ln -fs {rel}{no_ext} {link}')

    ops = [
        r1.succeeded, r2.succeeded, r3.succeeded, r4.succeeded
    ]

    sudo('service nginx reload')

    return True if all(ops) else False
