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
The controller uses POX.
```bash
./pox.py forwarding.l2_learning
```

## Flow Rule Management
Based on MAC addresses and ports:
```bash
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
```bash
iperf h1 h3
```
