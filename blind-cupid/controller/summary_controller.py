from utils import url_argument_validator as url_val
from flask import Flask, request, Response


def setup(app:Flask)->None:

    @app.route('/summary', methods=['GET'])
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
    if (not url_val.validate_argument_string(repo)): #just for testing null strings, ideally would be a DB check or smth
        return False
    return True

def check_valid_user(user:str) -> bool:
    if (not url_val.validate_argument_string(user)):
        return False
    #URL string is valid and can be further checked
    return is_registered_user

def is_registered_user(user:str) -> bool:
    return True