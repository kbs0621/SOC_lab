# 🔐 End-to-End SOC Lab: Attack Detection & Automated Response

## 📌 Project Overview

This project simulates real-world cyber attacks and builds an end-to-end Security Operations Center (SOC) detection and response pipeline.

The objective was not only to collect logs but to:
- Reproduce real attacks
- Design detection logic
- Compare SIEM platforms
- Implement automated response (SOAR-style)

---

## 🏗 Architecture

[Kali Attacker]
        ↓
[Ubuntu Server]
    ├─ UFW Log
    ├─ auth.log
    └─ Apache access.log
        ↓
[Filebeat]
        ↓
[Elasticsearch]
        ↓
[Kibana Detection Rules]
        ↓
[Alert Trigger]
        ↓
[Python SOAR API]
        ↓
[UFW Auto Block]

---

## 🛠 Tech Stack

- Kali Linux (Attack Simulation)
- Ubuntu 24.04 Server
- UFW Firewall
- Filebeat 8.x
- Elasticsearch 8.x
- Kibana (Security Detection Engine)
- Splunk Enterprise (Rule Comparison)
- FastAPI (Python SOAR Server)

---

# 🚨 Attack Scenarios

---

## 1️⃣ SSH Brute Force Detection

### Attack
Hydra-based password brute force.

### Log Source
/var/log/auth.log

### Detection Logic (Elastic)

Query:
