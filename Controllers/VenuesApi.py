from flask import Flask, Blueprint, jsonify, request
from flask_restx import Api, Resource, fields, Namespace
import uuid
# from app import api

venues_api = Blueprint('venue_details', __name__)
# venues_api = Namespace('Venues', description='API for managing venues')


# venues = []

# @venues_api.route('/venues')
# class Venues(Resource):
#     @venues_api.doc(description='Get venue details')
#     def get(self):
#         return jsonify(venues)

#     @venues_api.doc(description='Create a new venue')
#     def post(self):
#         data = request.json

#         venue_id = str(uuid.uuid4())
#         data['id'] = venue_id

#         venues.append(data)

#         return jsonify({'message': 'Venue created successfully', 'id': venue_id}), 201

# @venues_api.route('/venues/<venue_id>')
# @venues_api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @venues_api.doc(description='Get a venue')
#     def get(self, venue_id):
#         venue = next((v for v in venues if v['id'] == venue_id), None)

#         if venue:
#             return jsonify(venue)
#         else:
#             return jsonify({'message': 'Venue not found'}), 404

#     @venues_api.doc(description='Update a venue')
#     def put(self, venue_id):
#         data = request.json

#         venue = next((v for v in venues if v['id'] == venue_id), None)

#         if venue:
#             venue.update(data)
#             return jsonify({'message': 'Venue updated successfully'})
#         else:
#             return jsonify({'message': 'Venue not found'}), 404

#     @venues_api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         venue = next((v for v in venues if v['id'] == venue_id), None)

#         if venue:
#             venues.remove(venue)
#             return jsonify({'message': 'Venue deleted successfully'})
#         else:
#             return jsonify({'message': 'Venue not found'}), 404

#############

# @venues_api.route('/venues')
# class Venues(Resource):
#     @venues_api.route('/venues', methods=['POST'])
#     def create_line():
            
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue_id = str(uuid.uuid4())
#         data['id'] = venue_id

#         container.create_item(body=data)

#         return jsonify({'message': 'venue created successfully', 'id': venue_id}), 201

#     @venues_api.route('/venues/<venue_id>', methods=['PUT'])
#     def update_venue(venue_id):
        
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             for key, value in data.items():
#                 venue[key] = value

#             container.replace_item(item=venue_id, body=venue)

#             return jsonify({'message': 'venue updated successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @venues_api.route('/venues/<venue_id>', methods=['DELETE'])
#     def delete_venue(venue_id):
        
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             container.delete_item(item=venue_id, partition_key=venue_id)

#             return jsonify({'message': 'venue deleted successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @venues_api.route('/venues/<venue_id>', methods=['GET'])
#     def get_venue(venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = f'SELECT * FROM VENUES s WHERE s.id = "{venue_id}"'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         if len(venues) > 0:
#             return jsonify(venues[0])  
#         else:
#             return jsonify({'message': 'venue not found'}), 404
    
    ####################
# api = Api(venues_api)

# @api.route('/venues')
# class Venues(Resource):
#     @api.doc(description='Get venue details')
#     def get(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = 'SELECT * FROM VENUES'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         return jsonify(venues)

#     @api.doc(description='Create a new venue')
#     def post(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue_id = str(uuid.uuid4())
#         data['id'] = venue_id

#         container.create_item(body=data)

#         return jsonify({'message': 'venue created successfully', 'id': venue_id}), 201

# @api.route('/venues/<venue_id>')
# @api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @api.doc(description='Update a venue')
#     def put(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             for key, value in data.items():
#                 venue[key] = value

#             container.replace_item(item=venue_id, body=venue)

#             return jsonify({'message': 'venue updated successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             container.delete_item(item=venue_id, partition_key=venue_id)

#             return jsonify({'message': 'venue deleted successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @api.doc(description='Get a venue')
#     def get(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = f'SELECT * FROM VENUES s WHERE s.id = "{venue_id}"'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         if len(venues) > 0:
#             return jsonify(venues[0])
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#################

# @venues_api.route('/venues')
# class Venues(Resource):
#     def get(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = 'SELECT * FROM VENUES'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         return jsonify(venues)

#     def post(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue_id = str(uuid.uuid4())
#         data['id'] = venue_id

#         container.create_item(body=data)

#         return jsonify({'message': 'venue created successfully', 'id': venue_id}), 201

# @venues_api.route('/venues/<venue_id>')
# class Venue(Resource):
#     def put(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             for key, value in data.items():
#                 venue[key] = value

#             container.replace_item(item=venue_id, body=venue)

#             return jsonify({'message': 'venue updated successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     def delete(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             container.delete_item(item=venue_id, partition_key=venue_id)

#             return jsonify({'message': 'venue deleted successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     def get(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = f'SELECT * FROM VENUES s WHERE s.id = "{venue_id}"'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         if len(venues) > 0:
#             return jsonify(venues[0])
#         else:
#             return jsonify({'message': 'venue not found'}), 404
        
###################

# @api.route('/venues')
# class Venues(Resource):
#     @api.doc(description='Get venue details')
#     def get(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = 'SELECT * FROM VENUES'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         return jsonify(venues)

#     @api.doc(description='Create a new venue')
#     def post(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue_id = str(uuid.uuid4())
#         data['id'] = venue_id

#         container.create_item(body=data)

#         return jsonify({'message': 'venue created successfully', 'id': venue_id}), 201

# @api.route('/venues/<venue_id>')
# @api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @api.doc(description='Update a venue')
#     def put(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         data = request.json

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             for key, value in data.items():
#                 venue[key] = value

#             container.replace_item(item=venue_id, body=venue)

#             return jsonify({'message': 'venue updated successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         venue = container.read_item(item=venue_id, partition_key=venue_id)

#         if venue:
#             container.delete_item(item=venue_id, partition_key=venue_id)

#             return jsonify({'message': 'venue deleted successfully'})
#         else:
#             return jsonify({'message': 'venue not found'}), 404

#     @api.doc(description='Get a venue')
#     def get(self, venue_id):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = f'SELECT * FROM VENUES s WHERE s.id = "{venue_id}"'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         if len(venues) > 0:
#             return jsonify(venues[0])
#         else:
#             return jsonify({'message': 'venue not found'}), 404

# api.add_resource(Venues, '/venues')

# # api = Api(venues_api)


# venues_namespace = Namespace('venue_details', description='Operations related to venues')

# api.add_namespace(venues_namespace)
# venues_namespace.add_resource(VenueDetails, '')
# venues_namespace.add_resource(Venue, '/<venue_id>')


# @api.route('/venue_details')
# class VenueDetails(Resource):
#     @api.doc(description='Get venue details')
#     def get(self):
#         # Implement your GET logic here
#         return {'message': 'Get venue details'}

#     @api.doc(description='Create a new venue')
#     def post(self):
#         # Implement your POST logic here
#         return {'message': 'Create a new venue'}

# @api.route('/venues/<venue_id>')
# @api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @api.doc(description='Update a venue')
#     def put(self, venue_id):
#         # Implement your PUT logic here
#         return {'message': f'Update venue {venue_id}'}

#     @api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         # Implement your DELETE logic here
#         return {'message': f'Delete venue {venue_id}'}

#     @api.doc(description='Get a venue')
#     def get(self, venue_id):
#         # Implement your GET logic here
#         return {'message': f'Get venue {venue_id}'}


# @api.route('/venue_details')
# class VenueDetails(Resource):

#     @api.doc(description='Get venue details')
#     def get(self):
#         cosmos_client = venues_api.cosmos_client
#         cosmos_database = venues_api.cosmos_database
#         container = cosmos_database.get_container_client('VENUES')

#         query = 'SELECT * FROM VENUES'
#         venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#         return jsonify(venues)



#     @api.doc(description='Create a new venue')
#     def post(self):
#         # Implement your POST logic here
#         return {'message': 'Create a new venue'}

# @api.route('/venues/<venue_id>')
# @api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @api.doc(description='Update a venue')
#     def put(self, venue_id):
#         # Implement your PUT logic here
#         return {'message': f'Update venue {venue_id}'}

#     @api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         # Implement your DELETE logic here
#         return {'message': f'Delete venue {venue_id}'}

#     @api.doc(description='Get a venue')
#     def get(self, venue_id):
#         # Implement your GET logic here
#         return {'message': f'Get venue {venue_id}'}


#################
# @api.route('/venue_details')

# class VenueDetails(Resource):
#     @api.doc(description='Get venue details')
#     def get(self):
#         # Implement your GET logic here
#         return {'message': 'Get venue details'}

#     @api.doc(description='Create a new venue')
#     @api.expect(venue_model)
#     def post(self):
#         # Implement your POST logic here
#         return {'message': 'Create a new venue'}

# @api.route('/venues/<venue_id>')
# @api.param('venue_id', 'The unique identifier of the venue')
# class Venue(Resource):
#     @api.doc(description='Update a venue')

#     def put(self, venue_id):
#         # Implement your PUT logic here
#         return {'message': f'Update venue {venue_id}'}

#     @api.doc(description='Delete a venue')
#     def delete(self, venue_id):
#         # Implement your DELETE logic here
#         return {'message': f'Delete venue {venue_id}'}

#     @api.doc(description='Get a venue')
#     def get(self, venue_id):
#         # Implement your GET logic here
#         return {'message': f'Get venue {venue_id}'}

#################

@venues_api.route('/venues', methods=['GET'])
def get_venue_details():
    cosmos_client = venues_api.cosmos_client
    cosmos_database = venues_api.cosmos_database
    container = cosmos_database.get_container_client('VENUES')

    query = 'SELECT * FROM VENUES'
    venues = list(container.query_items(query=query, enable_cross_partition_query=True))

    return jsonify(venues)


# @venues_api.route('/venue_details', methods=['GET'])
# def get_venue_details():
#     cosmos_client = venues_api.cosmos_client
#     cosmos_database = venues_api.cosmos_database
#     container = cosmos_database.get_container_client('VENUES')

#     query = 'SELECT * FROM VENUES'
#     venues = list(container.query_items(query=query, enable_cross_partition_query=True))

#     return jsonify(venues)

@venues_api.route('/venues', methods=['POST'])
def create_line():
        
    cosmos_client = venues_api.cosmos_client
    cosmos_database = venues_api.cosmos_database
    container = cosmos_database.get_container_client('VENUES')

    data = request.json

    venue_id = str(uuid.uuid4())
    data['id'] = venue_id

    container.create_item(body=data)

    return jsonify({'message': 'venue created successfully', 'id': venue_id}), 201

@venues_api.route('/venues/<venue_id>', methods=['PUT'])
def update_venue(venue_id):
    
    cosmos_client = venues_api.cosmos_client
    cosmos_database = venues_api.cosmos_database
    container = cosmos_database.get_container_client('VENUES')

    data = request.json

    venue = container.read_item(item=venue_id, partition_key=venue_id)

    if venue:
        for key, value in data.items():
            venue[key] = value

        container.replace_item(item=venue_id, body=venue)

        return jsonify({'message': 'venue updated successfully'})
    else:
        return jsonify({'message': 'venue not found'}), 404

@venues_api.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    
    cosmos_client = venues_api.cosmos_client
    cosmos_database = venues_api.cosmos_database
    container = cosmos_database.get_container_client('VENUES')

    venue = container.read_item(item=venue_id, partition_key=venue_id)

    if venue:
        container.delete_item(item=venue_id, partition_key=venue_id)

        return jsonify({'message': 'venue deleted successfully'})
    else:
        return jsonify({'message': 'venue not found'}), 404

@venues_api.route('/venues/<venue_id>', methods=['GET'])
def get_venue(venue_id):
    cosmos_client = venues_api.cosmos_client
    cosmos_database = venues_api.cosmos_database
    container = cosmos_database.get_container_client('VENUES')

    query = f'SELECT * FROM VENUES s WHERE s.id = "{venue_id}"'
    venues = list(container.query_items(query=query, enable_cross_partition_query=True))

    if len(venues) > 0:
        return jsonify(venues[0])  
    else:
        return jsonify({'message': 'venue not found'}), 404
    
