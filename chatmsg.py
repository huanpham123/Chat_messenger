from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lưu trữ tin nhắn
messages = []

@app.route('/')
def index():
    return render_template('TH_AII.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    message = data.get('message')

    # Lưu tin nhắn vào danh sách
    messages.append({'sender': sender, 'message': message})

    return jsonify({'history': messages})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
