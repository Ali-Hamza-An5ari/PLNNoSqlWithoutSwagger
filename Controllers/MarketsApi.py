from flask import Flask, Blueprint, jsonify, request
import uuid

markets_api = Blueprint('markets', __name__)

@markets_api.route('/markets', methods=['GET'])
def get_markets():
    cosmos_client = markets_api.cosmos_client
    cosmos_database = markets_api.cosmos_database
    container = cosmos_database.get_container_client('MARKETS')

    query = 'SELECT * FROM MARKETS'
    markets = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(markets)

@markets_api.route('/markets', methods=['POST'])
def create_line():
        
    cosmos_client = markets_api.cosmos_client
    cosmos_database = markets_api.cosmos_database
    container = cosmos_database.get_container_client('MARKETS')

    data = request.json

    market_id = str(uuid.uuid4())
    data['id'] = market_id

    container.create_item(body=data)

    return jsonify({'message': 'market created successfully', 'id': market_id}), 201

@markets_api.route('/markets/<market_id>', methods=['PUT'])
def update_market(market_id):
    
    cosmos_client = markets_api.cosmos_client
    cosmos_database = markets_api.cosmos_database
    container = cosmos_database.get_container_client('MARKETS')

    data = request.json

    market = container.read_item(item=market_id, partition_key=market_id)

    if market:
        for key, value in data.items():
            market[key] = value

        container.replace_item(item=market_id, body=market)

        return jsonify({'message': 'market updated successfully'})
    else:
        return jsonify({'message': 'market not found'}), 404

@markets_api.route('/markets/<market_id>', methods=['DELETE'])
def delete_market(market_id):
    
    cosmos_client = markets_api.cosmos_client
    cosmos_database = markets_api.cosmos_database
    container = cosmos_database.get_container_client('MARKETS')

    market = container.read_item(item=market_id, partition_key=market_id)

    if market:
        container.delete_item(item=market_id, partition_key=market_id)

        return jsonify({'message': 'market deleted successfully'})
    else:
        return jsonify({'message': 'market not found'}), 404

@markets_api.route('/markets/<market_id>', methods=['GET'])
def get_market(market_id):
    cosmos_client = markets_api.cosmos_client
    cosmos_database = markets_api.cosmos_database
    container = cosmos_database.get_container_client('MARKETS')

    query = f'SELECT * FROM MARKETS s WHERE s.id = "{market_id}"'
    markets = list(container.query_items(query=query, enable_cross_partition_query=True))

    if len(markets) > 0:
        return jsonify(markets[0])  
    else:
        return jsonify({'message': 'market not found'}), 404
