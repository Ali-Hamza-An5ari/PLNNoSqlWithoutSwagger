from flask import Flask, Blueprint, jsonify, request
from dotenv import load_dotenv

import uuid

events_api = Blueprint('events_api', __name__)

@events_api.route('/scores', methods=['GET'])
def get_scores():
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    query = 'SELECT * FROM SCORES'
    scores = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(scores)

@events_api.route('/scores', methods=['POST'])
def create_line():
        
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    data = request.json

    score_id = str(uuid.uuid4())
    data['id'] = score_id
    container.create_item(body=data)

    return jsonify({'message': 'score created successfully', 'id': score_id}), 201

@events_api.route('/scores/<score_id>', methods=['PUT'])
def update_score(score_id):
    
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    # Get the data from the request
    data = request.json

    # Retrieve the score from the container
    score = container.read_item(item=score_id, partition_key=score_id)

    if score:
        # Update the score with the new data
        for key, value in data.items():
            score[key] = value

        # Replace the score in the container
        container.replace_item(item=score_id, body=score)

        return jsonify({'message': 'Score updated successfully'})
    else:
        return jsonify({'message': 'Score not found'}), 404

@events_api.route('/scores/<score_id>', methods=['DELETE'])
def delete_score(score_id):
    
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    # Retrieve the score from the container
    score = container.read_item(item=score_id, partition_key=score_id)

    if score:
        # Delete the score from the container
        container.delete_item(item=score_id, partition_key=score_id)

        return jsonify({'message': 'Score deleted successfully'})
    else:
        return jsonify({'message': 'Score not found'}), 404

@events_api.route('/scores/<score_id>', methods=['GET'])
def get_score(score_id):
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    # Query the container to retrieve the score by ID
    query = f'SELECT * FROM SCORES s WHERE s.id = "{score_id}"'
    scores = list(container.query_items(query=query, enable_cross_partition_query=True))

    if len(scores) > 0:
        return jsonify(scores[0])  # Return the score as JSON
    else:
        return jsonify({'message': 'Score not found'}), 404

@events_api.route('/scores/<event_status>', methods=['GET'])
def get_scores_by_event_status(event_status):
    cosmos_client = events_api.cosmos_client
    cosmos_database = events_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    # Query the container to retrieve scores by event status
    query = f'SELECT * FROM SCORES s WHERE s.event_status = "{event_status}"'
    scores = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(scores)