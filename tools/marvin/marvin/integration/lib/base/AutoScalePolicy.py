# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from marvin.integration.lib.base import CloudStackEntity
from marvin.cloudstackAPI import createAutoScalePolicy
from marvin.cloudstackAPI import updateAutoScalePolicy
from marvin.cloudstackAPI import deleteAutoScalePolicy

class AutoScalePolicy(CloudStackEntity):


    def __init__(self, items):
        self.__dict__.update(items)


    @classmethod
    def create(cls, apiclient, AutoScalePolicyFactory, **kwargs):
        cmd = createAutoScalePolicy.createAutoScalePolicyCmd()
        [setattr(cmd, factoryKey, factoryValue) for factoryKey, factoryValue in AutoScalePolicyFactory.attributes()]
        [setattr(cmd, key, value) for key,value in kwargs.items]
        autoscalepolicy = apiclient.createAutoScalePolicy(cmd)
        return AutoScalePolicy(autoscalepolicy.__dict__)


    def update(self, apiclient, id, **kwargs):
        cmd = updateAutoScalePolicy.updateAutoScalePolicyCmd()
        cmd.id = id
        [setattr(cmd, key, value) for key,value in kwargs.items]
        autoscalepolicy = apiclient.updateAutoScalePolicy(cmd)


    def delete(self, apiclient, id, **kwargs):
        cmd = deleteAutoScalePolicy.deleteAutoScalePolicyCmd()
        cmd.id = id
        [setattr(cmd, key, value) for key,value in kwargs.items]
        autoscalepolicy = apiclient.deleteAutoScalePolicy(cmd)

