# Detection Design Notes

## 🎯 Project Objective

This project goes beyond simple log collection.

The goal was to design and implement an end-to-end SOC workflow:

Attack Simulation → Log Analysis → Detection Logic Design → Automated Response

---

## 🧠 Core Detection Design Principles

### 1️⃣ Avoid Single-Event Alerts

- A single failed login may simply be a user mistake.
- Alerting on individual events increases false positives.
- Therefore, threshold-based aggregation was applied.

---

### 2️⃣ Use Threshold-Based Aggregation

Detection rules were designed to identify repeated behaviors within a defined time window.

Examples:
- SSH login failures ≥ 3 within 5 minutes
- Multiple blocked connections across different ports

This approach helps distinguish normal activity from malicious patterns.

---

### 3️⃣ Leverage Unique Value Aggregation (Port Scan Detection)

Instead of detecting traffic volume alone, the focus was on diversity of target ports.

Example:
- Unique destination.port ≥ 10

This differentiates repeated access attempts from true scanning behavior.

---

### 4️⃣ Consider False Positive Reduction

Detection tuning considered:

- Legitimate user login mistakes
- Internal test traffic
- Administrator access behavior
- Service-specific characteristics

Threshold values were adjusted to balance detection accuracy and noise reduction.

---

### 5️⃣ Design with Response Automation in Mind

Security monitoring does not end with detection.

The architecture was extended to include:

Alert → Webhook → Python SOAR → UFW Auto-Block

This ensured the project reflects real-world SOC thinking:
Detection + Response.

---

## 🔍 SIEM Platform Comparison

Both Elastic and Splunk were implemented and compared in terms of:

- Rule creation methodology
- Aggregation logic
- Alerting workflows
- Query language differences (KQL vs SPL)

This strengthened vendor-neutral detection design capability.

---

## 🔐 Key Insights Gained

- Raw logs require parsing and normalization.
- Detection logic design is more than query syntax.
- Threshold tuning is critical.
- Reducing false positives requires contextual thinking.
- Automated response enhances operational maturity.

---

## 📌 Conclusion

This project demonstrates:

- Hands-on attack reproduction
- Log analysis and normalization
- Detection logic engineering
- SIEM platform comparison
- Response automation design

It reflects practical SOC engineering capability beyond basic log monitoring.
