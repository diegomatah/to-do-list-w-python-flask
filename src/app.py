from flask import Flask,jsonify, request,json
app = Flask(__name__)



@app.route('/todos', methods=['GET'])

def hello_world():
    json_text = jsonify(todos)
    return json_text


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  json_text = jsonify(todos)
  print("This is the position to delete: ",position)
  return json_text  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)