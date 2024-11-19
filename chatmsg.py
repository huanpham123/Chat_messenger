from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dữ liệu lưu trữ phòng chat (được lưu trong memory)
chat_rooms = {"default": []}  # Mặc định có một phòng chat

@app.route('/')
def home():
    return render_template('TH_AII.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        sender = data.get('sender')
        message = data.get('message')
        room = "default"  # Luôn sử dụng phòng mặc định

        # Thêm tin nhắn vào lịch sử phòng chat
        chat_rooms[room].append({'sender': sender, 'message': message})
        return jsonify({'history': chat_rooms[room]}), 200
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

@app.route('/get_messages', methods=['GET'])
def get_messages():
    try:
        room = "default"  # Luôn sử dụng phòng mặc định

        # Trả về lịch sử tin nhắn của phòng chat
        return jsonify(chat_rooms[room]), 200
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
