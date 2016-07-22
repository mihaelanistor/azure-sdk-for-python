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


class EffectiveNetworkSecurityGroup(Model):
    """Effective NetworkSecurityGroup.

    :param network_security_group: Gets the id of network security group that
     is applied
    :type network_security_group: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param association:
    :type association: :class:`EffectiveNetworkSecurityGroupAssociation
     <azure.mgmt.network.models.EffectiveNetworkSecurityGroupAssociation>`
    :param effective_security_rules: Gets collection of effective security
     rules
    :type effective_security_rules: list of
     :class:`EffectiveNetworkSecurityRules
     <azure.mgmt.network.models.EffectiveNetworkSecurityRules>`
    """ 

    _attribute_map = {
        'network_security_group': {'key': 'networkSecurityGroup', 'type': 'SubResource'},
        'association': {'key': 'association', 'type': 'EffectiveNetworkSecurityGroupAssociation'},
        'effective_security_rules': {'key': 'effectiveSecurityRules', 'type': '[EffectiveNetworkSecurityRules]'},
    }

    def __init__(self, network_security_group=None, association=None, effective_security_rules=None):
        self.network_security_group = network_security_group
        self.association = association
        self.effective_security_rules = effective_security_rules