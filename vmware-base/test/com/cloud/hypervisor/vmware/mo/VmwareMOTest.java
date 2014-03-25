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

package com.cloud.hypervisor.vmware.mo;

import com.cloud.hypervisor.vmware.util.VmwareContext;

/**
 * 
 * @author hadoop
 * vmware 测试
 */
public class VmwareMOTest {

	public static void main(String args[]) {
        try {
       	
        	//VmwareContext context = TestVmwareContextFactory.create("10.192.18.235", "Administrator", "1qaz@WSX");
        	VmwareContext context = TestVmwareContextFactory.create("10.196.37.1", "yuntest", "Cpic1234");
        	DatacenterMO dcMo = new DatacenterMO(context, "2701");
      
        
        	HostMO hostMo = new HostMO(context, dcMo.findHost("10.192.18.75"));

        	DatastoreMO dsMo = new DatastoreMO(context, dcMo.findDatastore("datastore1"));
        	
        	System.out.println("存储路径:"+dsMo.getDatastoreRootPath());
        	System.out.println("仓库大小:"+dsMo.getInventoryPath());

        	//hostMo.importVmFromOVF("/tmp/ubuntu-12.04.1-desktop-i386-nest-13.02.04.ovf", "Test123", dsMo, "thin");

        	
        	//VirtualMachineMO vmMo = dcMo.findVm("test");
        	
      
        	//Thread.sleep(10*60000);
        	//vmMo.removeAllSnapshots();
        	
        } catch (Exception e) {
        	e.printStackTrace();
        }
    }
}

