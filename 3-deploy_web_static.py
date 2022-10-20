#!/usr/bin/python3
"""creates an archive of the web servers and deploys it"""

from fabric.operations import put, run, sudo
from fabric.api import env


pack_web = __import__('1-pack_web_static')
deploy_web = __import__('2-do_deploy_web_static')
env.hosts = ['44.210.15.126', '3.230.162.118']

def deploy():
    """creates an archive of the web servers and deploys it"""


    archive = pack_web.do_pack()
    if not archive:
        return False

    result = deploy_web.do_deploy(archive)

    return result
