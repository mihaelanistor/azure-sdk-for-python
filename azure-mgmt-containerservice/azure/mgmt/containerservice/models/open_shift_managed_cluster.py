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

from .resource import Resource


class OpenShiftManagedCluster(Resource):
    """OpenShift Managed cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param plan: Define the resource plan as required by ARM for billing
     purposes
    :type plan: ~azure.mgmt.containerservice.models.PurchasePlan
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response.
    :vartype provisioning_state: str
    :param open_shift_version: Required. Version of OpenShift specified when
     creating the cluster.
    :type open_shift_version: str
    :param public_hostname: Optional user-specified FQDN for OpenShift API
     server.
    :type public_hostname: str
    :param fqdn: User-specified FQDN for OpenShift API server loadbalancer
     internal hostname.
    :type fqdn: str
    :param network_profile: Configuration for OpenShift networking.
    :type network_profile: ~azure.mgmt.containerservice.models.NetworkProfile
    :param router_profiles: Configuration for OpenShift router(s).
    :type router_profiles:
     list[~azure.mgmt.containerservice.models.OpenShiftRouterProfile]
    :param master_pool_profile: Configuration for OpenShift master VMs.
    :type master_pool_profile:
     ~azure.mgmt.containerservice.models.OpenShiftManagedClusterMasterPoolProfile
    :param agent_pool_profiles: Configuration of OpenShift cluster VMs.
    :type agent_pool_profiles:
     list[~azure.mgmt.containerservice.models.OpenShiftManagedClusterAgentPoolProfile]
    :param auth_profile: Configures OpenShift authentication.
    :type auth_profile:
     ~azure.mgmt.containerservice.models.OpenShiftManagedClusterAuthProfile
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'open_shift_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'plan': {'key': 'plan', 'type': 'PurchasePlan'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'open_shift_version': {'key': 'properties.openShiftVersion', 'type': 'str'},
        'public_hostname': {'key': 'properties.publicHostname', 'type': 'str'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'router_profiles': {'key': 'properties.routerProfiles', 'type': '[OpenShiftRouterProfile]'},
        'master_pool_profile': {'key': 'properties.masterPoolProfile', 'type': 'OpenShiftManagedClusterMasterPoolProfile'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[OpenShiftManagedClusterAgentPoolProfile]'},
        'auth_profile': {'key': 'properties.authProfile', 'type': 'OpenShiftManagedClusterAuthProfile'},
    }

    def __init__(self, **kwargs):
        super(OpenShiftManagedCluster, self).__init__(**kwargs)
        self.plan = kwargs.get('plan', None)
        self.provisioning_state = None
        self.open_shift_version = kwargs.get('open_shift_version', None)
        self.public_hostname = kwargs.get('public_hostname', None)
        self.fqdn = kwargs.get('fqdn', None)
        self.network_profile = kwargs.get('network_profile', None)
        self.router_profiles = kwargs.get('router_profiles', None)
        self.master_pool_profile = kwargs.get('master_pool_profile', None)
        self.agent_pool_profiles = kwargs.get('agent_pool_profiles', None)
        self.auth_profile = kwargs.get('auth_profile', None)
