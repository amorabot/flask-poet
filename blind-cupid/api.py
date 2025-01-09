from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/')
def serve_root():
    return app.send_static_file('index.html')


#Test route!
@app.route('/<name>')
def my_view_func(name):
    return name


#/foo?usuario=...&repositorio=...
@app.route('/profile', methods=['GET'])
def serve_user_profile() -> Response:
    args = request.args
    username = args.get('usuario', default = '', type=str)
    if (not check_valid_user(user=username)):
        return {
            "user":"Invalid"
        }, 400
    
    repository = args.get('repositorio', default = '', type=str)
    #Check repo...
    if (not check_valid_repo(repo=repository)):
        return {
            "user":username,
            "repository": "Invalid",
            "authors": None
        }, 400

    return {
            "user":username,
            "repository": repository,
            "authors": [build_author_data("Daniel Amorim", 0.87), build_author_data("Rafael Bamberg", 4.20), build_author_data("Diogo Lima", 13.0)]
        }, 200

def build_author_data(author_username:str, commit_avg:float)-> dict:
    return {
        "name": author_username,
        "commits-per-day": commit_avg
    }


#Do error handling for all checks
def check_valid_repo(repo:str) -> bool:
    if (not validate_argument_string(repo)): #just for testing null strings, ideally would be a DB check or smth
        return False
    return True

def check_valid_user(user:str) -> bool:
    if (not validate_argument_string(user)):
        return False
    #URL string is valid and can be further checked
    return is_registered_user

def is_registered_user(user:str) -> bool:
    return True


#/foo/bar?user1=...&user2=...&user3=...
@app.route('/search', methods=['GET'])
def search_users() -> Response:
    if (not validate_search_query(request)):
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


def validate_search_query(request) -> bool:
    #Check if at least one of the user is valid/not null to be queried
    args = request.args
    user1_valid: bool = validate_argument_string(args.get('user1', default = '', type=str))
    user2_valid: bool = validate_argument_string(args.get('user2', default = '', type=str))
    user3_valid: bool = validate_argument_string(args.get('user3', default = '', type=str))
    return (user1_valid or user2_valid or user3_valid)

def validate_argument_string(user_argument:str) -> bool:
    print("Validating user:")
    print(user_argument)
    invalid_user: bool = (user_argument == None) or (user_argument.strip() == '')
    return not invalid_user
    



if __name__ == "__main__":
    app.run(debug=True)