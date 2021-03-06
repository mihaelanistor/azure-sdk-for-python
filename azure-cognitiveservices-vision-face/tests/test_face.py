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
from os.path import dirname, join, realpath

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import Gender
from msrest.authentication import CognitiveServicesCredentials

from azure_devtools.scenario_tests import ReplayableTest, AzureTestError

from devtools_testutils import mgmt_settings_fake as fake_settings

CWD = dirname(realpath(__file__))

class FaceTest(ReplayableTest):
    FILTER_HEADERS = ReplayableTest.FILTER_HEADERS + ['Ocp-Apim-Subscription-Key']

    def __init__(self, method_name):
        self._fake_settings, self._real_settings = self._load_settings()
        super(FaceTest, self).__init__(method_name)

    @property
    def settings(self):
        if self.is_live:
            if self._real_settings:
                return self._real_settings
            else:
                raise AzureTestError('Need a mgmt_settings_real.py file to run tests live.')
        else:
            return self._fake_settings

    def _load_settings(self):
        try:
            from devtools_testutils import mgmt_settings_real as real_settings
            return fake_settings, real_settings
        except ImportError:
            return fake_settings, None

    def test_face_detect(self):
        credentials = CognitiveServicesCredentials(
            self.settings.CS_SUBSCRIPTION_KEY
        )
        face_client = FaceClient("https://westus2.api.cognitive.microsoft.com", credentials=credentials)
        with open(join(CWD, "facefindsimilar.queryface.jpg"), "rb") as face_fd:
            result = face_client.face.detect_with_stream(
                face_fd,
                return_face_attributes=['age','gender','headPose','smile','facialHair','glasses','emotion','hair','makeup','occlusion','accessories','blur','exposure','noise']
            )

        detected = result[0]
        self.assertEquals(detected.face_attributes.age, 52.4)
        self.assertEquals(detected.face_attributes.gender, Gender.female)
        self.assertEquals(detected.face_attributes.emotion.happiness, 1.0)
