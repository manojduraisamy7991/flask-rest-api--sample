from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
students = [
    {'id': 1, 'name': 'John Doe', 'major': 'Computer Science'},
    {'id': 2, 'name': 'Jane Smith', 'major': 'Data Science'},
    {'id': 3, 'name': 'Bob Johnson', 'major': 'Electrical Engineering'}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

if __name__ == '__main__':
    app.run()
