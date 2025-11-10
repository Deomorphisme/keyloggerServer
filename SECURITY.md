# Security Policy

## **1. Overview**
- **Project Purpose**: Logs keystrokes for **authorized** research/red teaming/debugging.
- **Risk Acknowledgment**: Misuse violates privacy laws (e.g., GDPR, Wiretap Act).
- **Intended Use**: Ethical testing with **explicit consent** from monitored users.
- **Liability**: Pentesters/users assume full legal responsibility for misuse.
- **Transparency**: All participants must be informed of data collection.

---

## **2. Security Risks & Mitigations**

### **2.1 Data Storage**
- **Risk**: Unencrypted logs in `logs.db` expose sensitive input.
- **Mitigation**:
  - Encrypt database (`sqlite3` → `SQLCipher`).
  - Store logs in memory-only tables (ephemeral).
  - Implement automatic purging (e.g., 24-hour retention).
- **Access Control**:
  - Restrict `logs.db` permissions (`chmod 600`).
  - Disable SQLite remote access.

### **2.2 Transmission Security**
- **Risk**: Plaintext WebSocket/HTTP leaks data in transit.
- **Mitigation**:
  - Enforce TLS (`socketio.run(..., ssl_context='adhoc')`).
  - Validate origins (`cors_allowed_origins=["https://trusted-domain.com"]`).
  - Rate-limit endpoints to prevent flooding.

### **2.3 Authentication & Authorization**
- **Risk**: No auth allows unauthorized log injection.
- **Mitigation**:
  - Require API keys for `/log` endpoint.
  - Implement JWT for WebSocket connections.
  - Log client IPs for audit trails.

### **2.4 Legal & Ethical Compliance**
- **Risk**: Non-compliance with privacy laws (e.g., GDPR, CCPA).
- **Mitigation**:
  - **Consent**: Obtain written approval from monitored users.
  - **Anonymization**: Strip PII (e.g., passwords, credit cards) pre-storage.
  - **Jurisdiction**: Comply with local surveillance laws (e.g., EU’s ePrivacy Directive).

### **2.5 Code-Level Risks**
- **Risk**: Hardcoded `SECRET_KEY` enables session hijacking.
- **Mitigation**:
  - Use environment variables (`os.getenv('SECRET_KEY')`).
  - Rotate keys periodically.
- **Risk**: SQL injection via `insert_log`.
  - **Mitigation**: Use parameterized queries (already implemented).

---

## **3. Incident Response**
- **Data Breach**:
  1. Isolate server (`systemctl stop keylogger`).
  2. Notify affected users within 72 hours (GDPR requirement).
  3. Delete compromised logs.
- **Legal Requests**:
  - Cooperate with law enforcement if subpoenaed.
  - Provide logs **only** with valid court orders.

---

## **4. Ethical Guidelines**
- **Do Not**:
  - Deploy without consent.
  - Target third parties (e.g., public Wi-Fi users).
  - Store logs longer than necessary.
- **Do**:
  - Document all testing with timestamps/participant names.
  - Use in controlled environments (e.g., lab machines).
  - Provide opt-out mechanisms for users.

---

## **5. Disclosure Policy**
- **Vulnerabilities**: Report to [your-contact-email] via GPG-encrypted email.
- **Responsible Disclosure**:
  - 90-day window for fixes before public disclosure.
  - Credit researchers in `CHANGELOG.md`.

---
**Final Note**:
This tool is **not** for surveillance. Violations may result in legal action.
Always prioritize **ethics over functionality**.