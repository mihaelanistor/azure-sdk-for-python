# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComputeNodeGetRemoteLoginSettingsResult(Model):
    """Response to a ComputeNodeOperation.GetRemoteLoginSettings request.

    :param remote_login_ip_address: The IP address used for remote login to
     the compute node.
    :type remote_login_ip_address: str
    :param remote_login_port: The port used for remote login to the compute
     node.
    :type remote_login_port: int
    """ 

    _validation = {
        'remote_login_ip_address': {'required': True},
        'remote_login_port': {'required': True},
    }

    _attribute_map = {
        'remote_login_ip_address': {'key': 'remoteLoginIPAddress', 'type': 'str'},
        'remote_login_port': {'key': 'remoteLoginPort', 'type': 'int'},
    }

    def __init__(self, remote_login_ip_address, remote_login_port):
        self.remote_login_ip_address = remote_login_ip_address
        self.remote_login_port = remote_login_port