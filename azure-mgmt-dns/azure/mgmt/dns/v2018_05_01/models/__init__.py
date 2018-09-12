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

try:
    from .arecord_py3 import ARecord
    from .aaaa_record_py3 import AaaaRecord
    from .mx_record_py3 import MxRecord
    from .ns_record_py3 import NsRecord
    from .ptr_record_py3 import PtrRecord
    from .srv_record_py3 import SrvRecord
    from .txt_record_py3 import TxtRecord
    from .cname_record_py3 import CnameRecord
    from .soa_record_py3 import SoaRecord
    from .caa_record_py3 import CaaRecord
    from .sub_resource_py3 import SubResource
    from .record_set_py3 import RecordSet
    from .record_set_update_parameters_py3 import RecordSetUpdateParameters
    from .zone_py3 import Zone
    from .zone_update_py3 import ZoneUpdate
    from .dns_resource_reference_request_py3 import DnsResourceReferenceRequest
    from .dns_resource_reference_py3 import DnsResourceReference
    from .dns_resource_reference_result_py3 import DnsResourceReferenceResult
    from .resource_py3 import Resource
except (SyntaxError, ImportError):
    from .arecord import ARecord
    from .aaaa_record import AaaaRecord
    from .mx_record import MxRecord
    from .ns_record import NsRecord
    from .ptr_record import PtrRecord
    from .srv_record import SrvRecord
    from .txt_record import TxtRecord
    from .cname_record import CnameRecord
    from .soa_record import SoaRecord
    from .caa_record import CaaRecord
    from .sub_resource import SubResource
    from .record_set import RecordSet
    from .record_set_update_parameters import RecordSetUpdateParameters
    from .zone import Zone
    from .zone_update import ZoneUpdate
    from .dns_resource_reference_request import DnsResourceReferenceRequest
    from .dns_resource_reference import DnsResourceReference
    from .dns_resource_reference_result import DnsResourceReferenceResult
    from .resource import Resource
from .record_set_paged import RecordSetPaged
from .zone_paged import ZonePaged
from .dns_management_client_enums import (
    ZoneType,
    RecordType,
)

__all__ = [
    'ARecord',
    'AaaaRecord',
    'MxRecord',
    'NsRecord',
    'PtrRecord',
    'SrvRecord',
    'TxtRecord',
    'CnameRecord',
    'SoaRecord',
    'CaaRecord',
    'SubResource',
    'RecordSet',
    'RecordSetUpdateParameters',
    'Zone',
    'ZoneUpdate',
    'DnsResourceReferenceRequest',
    'DnsResourceReference',
    'DnsResourceReferenceResult',
    'Resource',
    'RecordSetPaged',
    'ZonePaged',
    'ZoneType',
    'RecordType',
]