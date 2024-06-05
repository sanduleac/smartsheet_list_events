from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Define the path for the JSON file
json_file_path = os.path.join(os.getcwd(), 'changeAgent.json')

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        
        # Extract the change_agent information from headers
        change_agent = request.headers.get('change-agent', 'unknown')

        # Prepare the data to be saved
        change_agent_info = {
            "change_agent": change_agent,
            "data": data
        }

        # Save the data to a JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(change_agent_info, json_file, indent=4)

        return jsonify({"message": "Change agent information saved"}), 200
    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
