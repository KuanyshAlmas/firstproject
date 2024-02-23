import json

def get_profiles_from_file():
    with open("data.json", "r") as f:
        return json.load(f)
    
def set_profiles_to_file(data):
    with open("data.json", "w") as f:
        return json.dump(data, f)


def jsonify_response(obj, message =  "Request was handle succsessfully" ):
    return {
        "message": message,
        "result": obj
    }