# Web Brute Force Detection (Elastic)

## 📌 Log Source
Apache access.log

---

## 🔍 Detection Query (KQL)

user_agent.original : "*Hydra*"

OR

http.response.status_code : 401

---

## ⚙ Rule Configuration

- Group by: source.ip
- Threshold: >= 5
- Time Window: 5 minutes

---

## 🧠 Detection Design Rationale

- Automated tools often leave identifiable user-agent strings.
- Repeated HTTP 401 responses indicate credential guessing attempts.
