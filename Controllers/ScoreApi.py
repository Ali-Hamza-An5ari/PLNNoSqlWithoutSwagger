from flask import Blueprint, jsonify, request
import uuid

score_api = Blueprint('score_api', __name__)

@score_api.route('/scores', methods=['GET'])
def get_scores():
    cosmos_client = score_api.cosmos_client
    cosmos_database = score_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    query = 'SELECT * FROM SCORES'
    scores = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(scores)

@score_api.route('/scores', methods=['POST'])
def create_score():

    cosmos_client = score_api.cosmos_client
    cosmos_database = score_api.cosmos_database
    container = cosmos_database.get_container_client('SCORES')

    data = request.json

    score_id = str(uuid.uuid4())
    data['id'] = score_id
    container.create_item(body=data)

    return jsonify({'message': 'Score created successfully', 'id': score_id}), 201
