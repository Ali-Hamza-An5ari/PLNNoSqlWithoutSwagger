from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import uuid

load_dotenv()

lines_api = Blueprint('lines_api', __name__)

@lines_api.route('/lines', methods=['GET'])
def get_lines():
        
    cosmos_client = lines_api.cosmos_client
    cosmos_database = lines_api.cosmos_database
    container = cosmos_database.get_container_client('LINES')

    query = 'SELECT * FROM LINES'
    lines = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(lines)

@lines_api.route('/lines', methods=['POST'])
def create_line():
        
    cosmos_client = lines_api.cosmos_client
    cosmos_database = lines_api.cosmos_database
    container = cosmos_database.get_container_client('LINES')

    data = request.json

    line_id = str(uuid.uuid4())
    data['id'] = line_id

    # Insert the line into the container
    container.create_item(body=data)

    return jsonify({'message': 'Line created successfully', 'id': line_id}), 201

@lines_api.route('/lines/<line_id>', methods=['PUT'])
def update_line(line_id):
    
    cosmos_client = lines_api.cosmos_client
    cosmos_database = lines_api.cosmos_database
    container = cosmos_database.get_container_client('LINES')

    # Get the data from the request
    data = request.json

    line = container.read_item(item=line_id, partition_key=line_id)

    if line:
        for key, value in data.items():
            line[key] = value

        container.replace_item(item=line_id, body=line)

        return jsonify({'message': 'Line updated successfully'})
    else:
        return jsonify({'message': 'Line not found'}), 404

@lines_api.route('/lines/<line_id>', methods=['DELETE'])
def delete_line(line_id):
    
    cosmos_client = lines_api.cosmos_client
    cosmos_database = lines_api.cosmos_database
    container = cosmos_database.get_container_client('LINES')

    # Retrieve the line from the container
    line = container.read_item(item=line_id, partition_key=line_id)

    if line:
        # Delete the line from the container
        container.delete_item(item=line_id, partition_key=line_id)

        return jsonify({'message': 'Line deleted successfully'})
    else:
        return jsonify({'message': 'Line not found'}), 404