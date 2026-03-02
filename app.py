from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    try:
        # Evaluate the expression safely
        # Only allow digits and operators
        allowed_chars = '0123456789+-*/(). '
        if any(c not in allowed_chars for c in expression):
            return jsonify({'error': 'Invalid characters in expression'}), 400
        result = eval(expression, {'__builtins__': None}, {})
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
