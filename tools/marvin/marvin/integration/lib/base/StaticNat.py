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
from marvin.cloudstackAPI import enableStaticNat
from marvin.cloudstackAPI import disableStaticNat

class StaticNat(CloudStackEntity.CloudStackEntity):


    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


    def enable(self, apiclient, ipaddressid, virtualmachineid, **kwargs):
        cmd = enableStaticNat.enableStaticNatCmd()
        cmd.ipaddressid = ipaddressid
        cmd.virtualmachineid = virtualmachineid
        [setattr(cmd, key, value) for key,value in kwargs.items]
        staticnat = apiclient.enableStaticNat(cmd)


    def disable(self, apiclient, ipaddressid, **kwargs):
        cmd = disableStaticNat.disableStaticNatCmd()
        cmd.ipaddressid = ipaddressid
        [setattr(cmd, key, value) for key,value in kwargs.items]
        staticnat = apiclient.disableStaticNat(cmd)

