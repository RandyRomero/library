#!python3
# -*- coding: utf-8 -*-
# to connect to remote MySQL DB
import sshtunnel
from .config import ssh_pswrd


def get_local_bind_port():
    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0
    tunnel = sshtunnel.SSHTunnelForwarder('ssh.pythonanywhere.com',
                                          ssh_username='OloloRodriguez',
                                          ssh_password=ssh_pswrd,
                                          remote_bind_address=('OloloRodriguez.mysql.pythonanywhere-services.com',
                                                               3306))

    tunnel.start()
    return tunnel.local_bind_port


get_local_bind_port()
print('SSH tunnel has been established')

# TODO Find a way how can we make Django close it when it is unneeded
