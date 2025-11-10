from flask_socketio import emit
from database import insert_log

def register_ws_handlers(socketio):
    @socketio.on('connect')
    def handle_connect():
        print('Client WebSocket connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client WebSocket disconnected')

    @socketio.on('log')
    def handle_ws_log(json):
        """Handler WebSocket pour les logs."""
        if not all(k in json for k in ['time_agent', 'host', 'ip', 'input']):
            emit('error', {'message': 'Missing required fields'})
            return

        if insert_log(json, method="WS"):
            emit('response', {'status': 'log received'})
        else:
            emit('error', {'message': 'Failed to store log'})
