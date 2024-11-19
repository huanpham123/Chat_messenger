from flask import Flask, render_template, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Dữ liệu chat (lưu trữ theo mật khẩu phòng)
chat_rooms = defaultdict(list)

@app.route('/')
def index():
    return render_template('TH_AII.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    message = data.get('message')
    password = data.get('123456')

    # Kiểm tra mật khẩu phòng, lưu tin nhắn vào phòng tương ứng
    if password:
        chat_rooms[password].append({'sender': sender, 'message': message})
        return jsonify({'history': chat_rooms[password]})
    return jsonify({'error': 'Invalid room password'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    password = request.args.get('password')
    if password and password in chat_rooms:
        return jsonify(chat_rooms[password])
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
