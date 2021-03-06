// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.
package com.cloud.agent.api;

import com.cloud.vm.VirtualMachine;
import com.cloud.vm.VirtualMachine.PowerState;

//
// TODO vmsync
// We should also have a HostVmStateReport class instead of using raw Map<> data structure,
// for now, we store host-specific info at each VM entry and host fields are fixed
// 
// This needs to be refactor-ed afterwards
//
public class HostVmStateReportEntry {
    VirtualMachine.PowerState state;
    
    // host name or host uuid
    String host;

    // XS needs Xen Tools version info
    String hostToolsVersion;
    
    public HostVmStateReportEntry() {
    }
    
    public HostVmStateReportEntry(PowerState state, String host, String hostToolsVersion) {
        this.state = state;
        this.host = host;
        this.hostToolsVersion = hostToolsVersion;
    }
    
    public PowerState getState() {
        return state;
    }
    
    public String getHost() {
        return host;
    }
    
    public String getHostToolsVersion() {
    	return hostToolsVersion;
    }
}
