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
from marvin.base import Zone
from marvin.factory import CloudStackBaseFactory
from marvin.utils import random_gen

class ZoneFactory(CloudStackBaseFactory):

    FACTORY_FOR = Zone

    dns1 = "8.8.8.8"
    internaldns1 = "8.8.8.8"
    name = None
    networktype = None

class AdvancedZoneFactory(ZoneFactory):
    name = factory.Sequence(lambda n: "advzone" + random_gen())
    networktype = "Advanced"

class BasicZoneFactory(ZoneFactory):
    name = factory.Sequence(lambda n: "basiczone" + random_gen())
    networktype = "Basic"

