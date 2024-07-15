from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

# link exceptions
app.config["PROPAGATE_EXCEPTIONS"] = True   
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
# where the root api is

app.config["OPENAPI_URL_PREFIX"] = "/"  

# ---- tell flask-smorest to use swagger
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" 
# api
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# ==> where to load the code
api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)