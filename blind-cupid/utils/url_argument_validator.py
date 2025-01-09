def validate_search_query(request) -> bool:
    #Check if at least one of the user is valid/not null to be queried
    args = request.args
    user1_valid: bool = validate_argument_string(args.get('user1', default = '', type=str))
    user2_valid: bool = validate_argument_string(args.get('user2', default = '', type=str))
    user3_valid: bool = validate_argument_string(args.get('user3', default = '', type=str))
    return (user1_valid or user2_valid or user3_valid)

def validate_argument_string(url_argument:str) -> bool:
    print("Validating argument string:")
    print(url_argument)
    invalid_arg: bool = (url_argument == None) or (url_argument.strip() == '')
    return not invalid_arg