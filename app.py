from flask import Flask
from flask_socketio import SocketIO
from routes.http import http_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ta_clé_secrète'

# Initialise SocketIO une seule fois
socketio = SocketIO(app, cors_allowed_origins="*", logger=True)

# Enregistre les routes HTTP
app.register_blueprint(http_blueprint)

# Import des handlers WebSocket (déclarés dans routes/ws.py)
from routes.ws import register_ws_handlers
register_ws_handlers(socketio)

if __name__ == '__main__':
    from database import init_db
    init_db()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
