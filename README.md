# Visual Network Configuration of Operation and Maintenance Based on SDN
## Rational
Because the traditional network management network equipment configuration is tedious, it needs to use the command line to configure one by one, manual operation will lead to the risk of operational errors; and the traditional network maintenance is difficult: the deployment of the new protocol and troubleshooting make network maintenance a very difficult task. In the SDN environment, SDN separates data from control by using the idea of hierarchy. In the control layer, including the logic centralized and programmable controller, it can master the global network information, facilitate operators and researchers to manage and configure the network and deploy new protocols. So we think about the visual network configuration and operation and maintenance in the SDN environment.

## Code Architecture
![总体构架](https://img-blog.csdnimg.cn/20200113124354198.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzkyNDg4NQ==,size_16,color_FFFFFF,t_70)

## 

- Overview of SDN Features 
  - Logical centralization
    - Logical centralization refers to the black box self-learning network equipment under the traditional network. In the SDN network environment, the separation of transfer control is realized: the control plane of the network element is on the controller, responsible for protocol calculation and generating flow tables; The forwarding plane is only on the network device. The control layer is the control center of the system, responsible for the generation of internal switching paths and border service routes of the network, and is responsible for handling network state change events.
   - Programmable
    - Directly control these hardware by compiling code to implement your own protocol or functionb. Northbound interface provides a series of rich APIs, on which developers can design their own applications without having to care about the underlying hardware details
    
