from flask_restful import Resource 

class UserAPI(Resource) :
    def get(self, username): 
        print("GET username", username)
        return {"username" : username}

    def put(self, username): 
        print("PUT username", username)
        return {"username" : username}

    def delete(self, username):
        print("DELETE username", username)
        return {"username" : username}

    def post(self): 
        print("POST username", username)
        return {"username" : username}

