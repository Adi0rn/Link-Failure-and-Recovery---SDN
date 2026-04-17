# Link Failure and Recovery - SDN mininet project

## Student details
- **Name:** Adithya Ajith Pillai
- **SRN:** PES2UG24AM014

## Problem Statement
This project demonstrates how Software Defined Networking (SDN) can detect link failures and automatically reroute traffic using alternate paths.

## Topology
2 Hosts and 3 Switches with redundant path.
```bash
sudo mn --topo linear,3 --controller=remote,ip=127.0.0.1,port=6633
```

## Controller
Implementation uses POX’s built-in L2 learning controller module instead of a custom controller.
```bash
cd pox
./pox.py forwarding.l2_learning
```

## Flow Rule Management
OpenFlow based flow rule management:
```bash
sh ovs-ofctl dump-flows s1
```

## Testing
**1. Normal:**
```bash
pingall
```

**2. Link Failure**
```bash
link s1 s2 down
pingall
```

**3. Recovery**
```bash
link s1 s2 up
pingall
```

## Performance
```bash
h3 iperf -s &
h1 iperf -c h3
h1 ping h3
```
