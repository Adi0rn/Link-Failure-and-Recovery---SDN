# Link Failure and Recovery - SDN mininet project

## Student details
- **Name:** Adithya Ajith Pillai
- **SRN:** PES2UG24AM014

## Problem Statement
This project demonstrates how Software Defined Networking (SDN) can detect link failures and automatically reroute traffic using alternate paths.

## Topology
Topology involves 2 hosts and 3 switches with backup path
```bash
sudo mn --custom topo.py --topo diamond --controller=remote
```

## Controller
Implementation uses POX’s built-in L2 learning controller module instead of a custom controller.
```bash
cd pox
~/pox$ nano topo.py
~/pox$ nano controller.py
~/pox$ sudo mn -c
```

## Flow Rule Management
OpenFlow based flow rule management:
```bash
pingall
sh ovs-ofctl dump-flows s1
pingall
dpctl dump-flows
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
**Throughput**
```bash
h2 iperf -s &
h1 iperf -c h2
```
**Latency**
```
h1 ping h2
```
