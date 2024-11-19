from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lưu trữ tin nhắn theo phòng chat (mật khẩu phòng là khóa)
chat_rooms = {}

@app.route('/')
def home():
    return render_template('TH_AII.html')  # Giao diện người dùng (HTML)

@app.route('/join', methods=['POST'])
def join_chat():
    try:
        # Nhận mật khẩu từ người dùng
        data = request.get_json()
        password = data.get('password')

        # Kiểm tra mật khẩu hợp lệ
        if not password:
            return jsonify({'error': 'sai mk'}), 400

        if password == "123456":  # Kiểm tra mật khẩu
            room = password
            if room not in chat_rooms:
                chat_rooms[room] = []  # Tạo phòng chat mới nếu chưa có
            return jsonify({'message': 'Success', 'room': room}), 200
        else:
            return jsonify({'error': 'Invalid password'}), 400
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Nhận dữ liệu từ người dùng (gửi tin nhắn)
        data = request.get_json()
        sender = data.get('sender')
        message = data.get('message')
        room = data.get('room')

        # Kiểm tra xem phòng chat có tồn tại không
        if not room or room not in chat_rooms:
            return jsonify({'error': 'Room not found'}), 400

        # Kiểm tra xem người gửi và tin nhắn có hợp lệ không
        if not sender or not message:
            return jsonify({'error': 'Sender or message is missing'}), 400

        # Lưu tin nhắn vào phòng chat
        chat_rooms[room].append({'sender': sender, 'message': message})
        return jsonify({'history': chat_rooms[room]}), 200

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        # Lấy tin nhắn trong phòng chat
        room = request.args.get('room')

        # Kiểm tra sự tồn tại của phòng chat
        if not room:
            return jsonify({'error': 'Room is required'}), 400

        if room in chat_rooms:
            return jsonify(chat_rooms[room]), 200
        else:
            return jsonify({'error': 'Room not found'}), 400
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
