# VPN Tunnel Implementation 

This project demonstrates how to implement a VPN tunnel using Python and Linux's TUN/TAP interfaces. It showcases the setup of a secure tunnel for routing IP packets between a client, server, and a private network.

---

## Features

- **TUN Interface Creation**: Simulates a network layer device for IP packet handling.
- **Packet Forwarding**: Routes packets between the client and private network via the VPN server.
- **ICMP Handling**: Processes ICMP (ping) requests and replies.

---

## Network Topology

The project uses three machines in a simulated Docker environment:

| Machine          | NAT Network IP | Internal Network IP |
|-------------------|----------------|----------------------|
| Host U (Client)   | `10.9.0.5`     | -                   |
| Gateway (Server)  | `10.9.0.11`    | `192.168.60.11`     |
| Host V (Private)  | -              | `192.168.60.5`      |

---

## Setup Instructions

### 1. Prerequisites

- Python 3.x
- Linux system with TUN/TAP support
- Docker and Docker Compose
- `Scapy` library (`pip install scapy`)

### 2. Clone the Repository

```bash
gh repo clone divyasharma0304/VPN-Tunnel-Implementation
```

### 3. Set Up the Docker Environment

```bash
docker-compose build
docker-compose up
dockps
docksh <id>
```


## Learn More

A detailed blog post explaining the project step-by-step is ([here](https://vpntunnel.hashnode.dev/building-a-vpn-tunnel)).

---

## References

- **SEED Labs**: VPN Lab Documentation by Wenliang Du ([link](https://seedsecuritylabs.org)).
