from flask import Flask, request, jsonify, render_template
from guardrail import PIGuard

app = Flask(__name__, template_folder='../templates')
guard = PIGuard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    result = guard.check(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)