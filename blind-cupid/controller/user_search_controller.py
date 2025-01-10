from utils import url_argument_validator as url_val
from flask import Flask, request,Response,jsonify

from model.user import user_repository
from model.models import User

def setup(app:Flask)->None:

    @app.route('/search', methods=['GET'])
    def search_users() -> Response:
        if (not url_val.validate_search_query(request)):
            # return Response("{'users':'No Valid users'}", status=400, mimetype='application/json')
            invalid_query_message: str = "No valid users! You need to submit at least 1 valid value!"
            return invalid_query_message, 400
        
        args = request.args

        user1 = args.get('user1', default = '', type=str)
        user2 = args.get('user2', default = '', type=str)
        user3 = args.get('user3', default = '', type=str)
        print("At least one valid arg!")
        response_json = jsonify({'users': [user1,user2,user3]})
        #When a valid JSON is sent as a response, Flask automatically sends a 200 HTTP code and the adequate response format
        #Its also possible to send a tuple as a response, the 1st arg is the JSON in the response's body and the 2nd is the HTTP code
        #https://flask.palletsprojects.com/en/stable/quickstart/#about-responses
        return response_json, 200
        # return Response(response_json, status=200, mimetype='application/json')

    
    @app.route('/user', methods=['GET'])
    def get_all_users()->Response:
        users: list[User] = user_repository.get_all_users()
        return {
            "users": stringify_users(users)
        }, 200
    


def stringify_users(users: list[User])->list[str]:
    stringified_users=[]
    for user in users:
        stringified_users.append(user.__repr__())
    return stringified_users