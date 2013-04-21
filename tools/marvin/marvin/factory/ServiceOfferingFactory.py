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
import factory
from marvin.base import ServiceOffering
from marvin.factory.CloudStackBaseFactory import *
from marvin.utils import random_gen

class ServiceOfferingFactory(CloudStackBaseFactory):

    FACTORY_FOR = ServiceOffering.ServiceOffering

    cpunumber = 1
    cpuspeed = 1000 #Mhz
    displaytext = "Service Offering"
    memory = 512 #MB
    name =  factory.Sequence(lambda n: "ServiceOffering" + random_gen())


class SmallServiceOfferingFactory(ServiceOfferingFactory):
    cpunumber = 1
    cpuspeed = 100 #Mhz
    memory = 100 #MB
    displaytext = "Small Service Offering"
    name = factory.Sequence(lambda n: "SmallServiceOffering" + random_gen())
