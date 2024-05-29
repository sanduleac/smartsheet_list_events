from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event_data = request.json

    # Print the entire event data to understand its structure
    print("Received event data:")
    print(event_data)

    # Example: Accessing specific fields in the event data
    for event in event_data.get('events', []):
        event_type = event.get('eventType')
        object_id = event.get('objectId')
        created_columns = event.get('createdColumns', [])

        print(f"Event Type: {event_type}")
        print(f"Object ID: {object_id}")

        for column in created_columns:
            column_id = column.get('id')
            column_title = column.get('title')
            column_type = column.get('type')

            print(f"Created Column ID: {column_id}")
            print(f"Created Column Title: {column_title}")
            print(f"Created Column Type: {column_type}")

    return jsonify({'message': 'Event received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
