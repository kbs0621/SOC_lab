# Port Scan Detection (Elastic)

## 📌 Log Source
UFW BLOCK logs

---

## 🔍 Detection Query (KQL)

event.action : "block"

---

## ⚙ Rule Configuration

- Rule Type: Threshold
- Group by: source.ip
- Threshold:
    - Count >= 10
    - Unique destination.port >= 10
- Time Window: 5 minutes

---

## 🧠 Detection Design Rationale

- Normal traffic may hit one or two blocked ports.
- Scanning behavior targets multiple ports.
- Using unique port count avoids false positives from repeated attempts to a single port.
