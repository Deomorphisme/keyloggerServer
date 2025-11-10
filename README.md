# Real-Time Log Collector

**Flask + SocketIO** service for capturing and storing logs via **HTTP** and **WebSocket**.

## Features
- **Multi-Protocol**: Accepts logs via:
  - **HTTP POST** (`/log` endpoint)
  - **WebSocket** (`log` event)
- **Structured Storage**: SQLite database with schema:
  ```sql
  logs (id, time_agent, time_server, method, host, ip, layout, input)
  ```
- **Validation**: Checks required fields (`time_agent`, `host`, `ip`, `input`).
- **Real-Time Feedback**: WebSocket emits `response`/`error` events.

## Setup
1. **Install Dependencies**:
   ```bash
   pip install flask flask-socketio
   ```
2. **Run Server**:
   ```bash
   python app.py  # Starts on 0.0.0.0:5000
   ```
3. **Database**: Auto-initializes `logs.db` on first run.

## Usage
### HTTP
```bash
curl -X POST http://localhost:5000/log \
  -H "Content-Type: application/json" \
  -d '{"time_agent": "2023-01-01", "host": "example.com", "ip": "192.168.1.1", "input": "test"}'
```
**Response**:
- `201 Success` or `400/500` for errors.

### WebSocket
```javascript
const socket = io('http://localhost:5000');
socket.emit('log', {
  time_agent: "2023-01-01",
  host: "example.com",
  ip: "192.168.1.1",
  input: "test"
});
```
**Events**:
- `response`: Confirmation on success.
- `error`: Missing fields or DB failure.

## Configuration
- **Secret Key**: Update `app.config['SECRET_KEY']` in production.
- **CORS**: Restrict `cors_allowed_origins` for production.
- **Database**: Modify `DB_NAME` in `database.py` if needed.

## Project Structure
```
.
├── app.py              # Flask/SocketIO app
├── database.py         # SQLite init/insert logic
├── routes/
│   ├── http.py         # HTTP endpoint (/log)
│   └── ws.py           # WebSocket handlers
└── logs.db             # Auto-created SQLite DB
```

## License
MIT