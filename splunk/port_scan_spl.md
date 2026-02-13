# Port Scan Detection (Splunk)

## SPL Query

index=soc_lab sourcetype=ufw_log action=block
| bucket _time span=5m
| stats dc(dest_port) as unique_ports count by src
| where unique_ports >= 10 AND count >= 20

---

## Explanation

- dc(dest_port): distinct count of destination ports
- Detects scanning across multiple ports
- Count ensures sustained scanning behavior
