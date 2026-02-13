# SSH Brute Force Detection (Splunk)

## SPL Query

index=soc_lab sourcetype=auth_log "Failed password"
| bucket _time span=5m
| stats count by src
| where count >= 3

---

## Explanation

- bucket: aggregate logs in 5-minute intervals
- stats count by src: count failures per IP
- where count >= 3: threshold condition
