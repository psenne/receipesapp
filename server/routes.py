from server import app, models, db
import json
from flask import Flask, jsonify, abort, make_response, request, send_from_directory
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS



Recipe = models.Recipe
User = models.User
Category = models.Category

user_schema = models.UserSchema()
users_schema = models.UserSchema(many=True)

recipe_schema = models.RecipeSchema()
recipes_schema = models.RecipeSchema(many=True)

################## CLIENT-SIDE ROUTES #################

@app.route("/", methods=['GET'])
def index():
    return send_from_directory('client/public', 'index.html')


# @app.route("/login", methods=['GET'])
# def login():
#     return send_from_directory('client/public', 'login.html')


@app.route("/test", methods=['GET'])
def test():
    return send_from_directory('', 'test.html')


@app.route("/images/<path:path>", methods=['GET'])
def images(path):
    return send_from_directory('images', path)


@app.route("/<path:path>", methods=['GET'])
def home(path):
    return send_from_directory('../client/public', path)


################## REST API #################
auth = HTTPBasicAuth()
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route("/api/checklogin", methods=['POST'])
def checklogin():
    print(request.json)
    token = request.json["accessToken"]
    u = User.query.filter_by(token=token).first_or_404()
    return user_schema.dump(u)



@app.route("/api/users", methods=['GET'])
def getusers():
    allusers = User.query.all()
    return jsonify(users_schema.dump(allusers))


@app.route("/api/user/<int:id>", methods=['GET'])
def getuser(id):
    u = User.query.filter_by(id=id).first_or_404()
    return user_schema.dump(u)


@app.route("/api/user/add", methods=['POST'])
def adduser():
    print('API created new user:')
    print(request.json)
    try:
        if not request.json or not 'email' in request.json:
            abort(400)

        u = User(name=request.json['name'], username=request.json['email'], email=request.json['email'])
        db.session.add(u)
        db.session.commit()
        return make_response(jsonify({"userid": u.id}), 200)

    except IntegrityError:
        return make_response(jsonify({"error": f"User {request.json['email']} already exists"}), 400)  # bad request

    except AttributeError as ae:
        print("User object error: %s" % ae)

    except TypeError as te:
        print("Type error: %s" % te)


@app.route("/api/recipes/", methods=['GET'])
def getrecipes():
    recipes = Recipe.query.all()
    return jsonify(recipes_schema.dump(recipes))


@app.route("/api/recipe/<int:id>", methods=['GET'])
def getrecipe(id):
    r = Recipe.query.filter_by(id=id).first_or_404()
    return recipe_schema.dump(r)



@app.route("/api/recipe/add", methods=['POST'])
def addrecipe():
    print("Adding new recipe...")
    try:
        if(request.json["title"] == ""):
            print("Error adding recipe. Recipe title is empty.")
            return make_response(jsonify({"success": "false", "reason": "Recipe title cannot be empty."}), 400)  # bad request

        r = Recipe(title=request.json['title'],
                   ingredients=request.json['ingredients'],
                   directions=request.json['directions'],
                   image=request.json['imageURL'],
                   user_id=1
                   )
        db.session.add(r)
        db.session.commit()

        request.json["success"] = "true"
        return make_response(jsonify(request.json), 200)

    except IntegrityError:
        return make_response(jsonify({"error": f"User {request.json['email']} already exists"}), 400)  # bad request

    except AttributeError as ae:
        print("User object error: %s" % ae)

    except TypeError as te:
        print("Type error: %s" % te)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Server Error: Unable to process request.'}), 500)
