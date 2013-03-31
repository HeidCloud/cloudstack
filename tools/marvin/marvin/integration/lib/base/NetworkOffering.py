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
from marvin.cloudstackAPI import createNetworkOffering
from marvin.cloudstackAPI import listNetworkOfferings
from marvin.cloudstackAPI import updateNetworkOffering
from marvin.cloudstackAPI import deleteNetworkOffering

class NetworkOffering(CloudStackEntity.CloudStackEntity):


    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


    @classmethod
    def create(cls, apiclient, NetworkOfferingFactory, **kwargs):
        cmd = createNetworkOffering.createNetworkOfferingCmd()
        [setattr(cmd, factoryKey, factoryValue) for factoryKey, factoryValue in NetworkOfferingFactory.__dict__.iteritems()]
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        networkoffering = apiclient.createNetworkOffering(cmd)
        return NetworkOffering(networkoffering.__dict__)


    @classmethod
    def list(self, apiclient, **kwargs):
        cmd = listNetworkOfferings.listNetworkOfferingsCmd()
        [setattr(cmd, key, value) for key,value in kwargs.items]
        networkoffering = apiclient.listNetworkOfferings(cmd)
        return map(lambda e: NetworkOffering(e.__dict__), networkoffering)


    def update(self, apiclient, **kwargs):
        cmd = updateNetworkOffering.updateNetworkOfferingCmd()
        [setattr(cmd, key, value) for key,value in kwargs.items]
        networkoffering = apiclient.updateNetworkOffering(cmd)


    def delete(self, apiclient, id, **kwargs):
        cmd = deleteNetworkOffering.deleteNetworkOfferingCmd()
        cmd.id = id
        [setattr(cmd, key, value) for key,value in kwargs.items]
        networkoffering = apiclient.deleteNetworkOffering(cmd)

