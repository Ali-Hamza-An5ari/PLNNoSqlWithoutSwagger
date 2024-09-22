# from flask import Flask
# import os
# from dotenv import load_dotenv
# from azure.cosmos import CosmosClient
# from flask_restx import Api, Resource, fields

# from flask_swagger_ui import get_swaggerui_blueprint
# from flask_swagger import swagger

# from Controllers.LinesApi import lines_api
# from Controllers.EventsApi import events_api
# from Controllers.MarketsApi import markets_api
# from Controllers.VenuesApi import venues_api#, Venues #, api

# load_dotenv()

# client = CosmosClient(os.getenv('ENDPOINT'), os.getenv('COSMOS_DB_KEY'))
# database = client.get_database_client(os.getenv('DATABASE_NAME'))

# app = Flask(__name__)

# SWAGGER_URL = '/swagger'
# API_URL = 'http://localhost:5000/swagger.json'

# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "PLN"
#     }
# )

# @app.route('/swagger.json')
# def swagger_json():
#     """Endpoint to generate the OpenAPI specification file."""
#     swag = swagger(app)
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "PLN API"
#     return swag

# cosmos_endpoint = os.getenv('ENDPOINT')
# cosmos_key = os.getenv('COSMOS_DB_KEY')
# cosmos_client = client

# cosmos_database_name = os.getenv('DATABASE_NAME')
# cosmos_database = cosmos_client.get_database_client(cosmos_database_name)

# events_api.cosmos_client = client
# events_api.cosmos_database = database
# lines_api.cosmos_client = client
# lines_api.cosmos_database = database
# markets_api.cosmos_client = client
# markets_api.cosmos_database = database
# venues_api.cosmos_client = client
# venues_api.cosmos_database = database

# # api.init_app(venues_api)
# api = Api(app)
# # api.add_namespace(venues_api)

# app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# app.register_blueprint(events_api, url_prefix='/api')
# app.register_blueprint(lines_api, url_prefix='/api')
# app.register_blueprint(markets_api, url_prefix='/api')
# app.register_blueprint(venues_api, url_prefix='/api')

# # api = Api(app, version='1.0', title='Venue API', description='API for managing venues')
# # api.add_namespace(venues_api)


# # api.add_resource(Venues, '/api/venues')

# # app.register_blueprint(venues_api)
# if __name__ == '__main__':
#     app.run(debug=True)


############

from flask import Flask
import os
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, PartitionKey
from flask_restx import Api, Namespace, Resource
# from flask_swagger_ui import get_swaggerui_blueprint
# from flask_swagger import swagger

load_dotenv()
client = CosmosClient(os.getenv('ENDPOINT'), os.getenv('COSMOS_DB_KEY'))

database = client.get_database_client(os.getenv('DATABASE_NAME'))

from Controllers.LinesApi import lines_api
from Controllers.EventsApi import events_api
from Controllers.MarketsApi import markets_api
from Controllers.VenuesApi import venues_api

app = Flask(__name__)

# SWAGGER_URL = '/swagger'
# API_URL = '/swagger.json'

# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "PLN"
#     }
# )

# @app.route('/swagger.json')
# def swagger_json():
#     """Endpoint to generate the OpenAPI specification file."""
#     swag = swagger(app)
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "PLN API"
#     return swag

cosmos_endpoint = os.getenv('ENDPOINT')
cosmos_key = os.getenv('COSMOS_DB_KEY')
cosmos_client = client

cosmos_database_name = os.getenv('DATABASE_NAME')
cosmos_database = cosmos_client.get_database_client(cosmos_database_name)

events_api.cosmos_client = client
events_api.cosmos_database = database
lines_api.cosmos_client = client
lines_api.cosmos_database = database
markets_api.cosmos_client = client
markets_api.cosmos_database = database
venues_api.cosmos_client = client
venues_api.cosmos_database = database

# app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(events_api, url_prefix='/api')
app.register_blueprint(lines_api, url_prefix='/api')
app.register_blueprint(markets_api, url_prefix='/api')
app.register_blueprint(venues_api, url_prefix='/api')


api = Api(app,
          title="PLN Swagger API",
          version="1.0",
          description="API for ",
          doc="/swagger/"
          )

todoNS = Namespace("todo", path="/todo", description="Todo namespace")
api.add_namespace(todoNS)

d = []

@todoNS.route('/todos')
class Todo(Resource):
    def get(self):
        return d
    def post(self):
        d.append(todoNS.payload)
        return d
    
if __name__ == '__main__':
    app.run(debug=True)

#####################

# from flask import Flask
# import os
# from dotenv import load_dotenv
# from azure.cosmos import CosmosClient, PartitionKey
# from flask_swagger import swagger
# from flask_swagger_ui import get_swaggerui_blueprint

# load_dotenv()
# client = CosmosClient(os.getenv('ENDPOINT'), os.getenv('COSMOS_DB_KEY'))


# database = client.get_database_client(os.getenv('DATABASE_NAME'))


# from Controllers.LinesApi import lines_api
# from Controllers.EventsApi import events_api
# from Controllers.MarketsApi import markets_api
# from Controllers.VenuesApi import venues_api

# app = Flask(__name__)


# swagger_config = swagger(app)

# @app.route('/swagger.json')
# def swagger_json():
#     """Endpoint to generate the OpenAPI specification file."""
#     return swagger_config
# SWAGGER_URL = '/swagger'
# API_URL = '/swagger.json'

# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "PLN"
#     }
# )

# cosmos_endpoint = os.getenv('ENDPOINT') 
# cosmos_key = os.getenv('COSMOS_DB_KEY') 
# cosmos_client = client 

# cosmos_database_name = os.getenv('DATABASE_NAME') 
# cosmos_database = cosmos_client.get_database_client(cosmos_database_name)

# events_api.cosmos_client = client
# events_api.cosmos_database = database
# lines_api.cosmos_client = client
# lines_api.cosmos_database = database
# markets_api.cosmos_client = client
# markets_api.cosmos_database = database
# venues_api.cosmos_client = client
# venues_api.cosmos_database = database

# app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# app.register_blueprint(events_api, url_prefix='/api')
# app.register_blueprint(lines_api, url_prefix='/api')
# app.register_blueprint(markets_api, url_prefix='/api')
# app.register_blueprint(venues_api, url_prefix='/api')
# if __name__ == '__main__':
#     app.run(debug=True)