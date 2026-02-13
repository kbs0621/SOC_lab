# SSH Brute Force Detection (Elastic)

## 📌 Log Source
/var/log/auth.log

Collected via Filebeat → Elasticsearch

---

## 🔍 Detection Query (KQL)

message : "Failed password"

---

## ⚙ Rule Configuration

- Rule Type: Threshold
- Group by: source.ip
- Threshold: >= 3
- Time Window: 5 minutes

---

## 🧠 Detection Design Rationale

- Single login failures may be legitimate user mistakes.
- Multiple failed attempts from the same IP indicate brute-force behavior.
- Threshold-based detection reduces false positives.

---

## 🚨 Expected Alert

If one source.ip generates 3 or more failed login attempts within 5 minutes,
an alert is triggered.
