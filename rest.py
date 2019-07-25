from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

songs = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 30,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]


class Song(Resource):
    def get(self, name=None):
        # if name == "All":
        return songs, 200
        # for song in songs:
        #     if name == song["name"]:
        #         return song, 200
        # return "User not Found", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for song in songs:
            if args["name"] == song["name"]:
                return "User with name {} already exists".format(args[name]), 400

        song = {
            "name": args["name"],
            "age": args["age"],
            "occupation": args["occupation"]
        }

        songs.append(song)
        return song, 201

    def put(self, name='Jass'):
        parser = reqparse.RequestParser()

        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for song in songs:
            if name == song["name"]:
                song["age"] = args["age"]
                song["occupation"] = args["occupation"]
                return song, 200

        song = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        songs.append(song)
        return song, 201

    def delete(self, name='Jass'):
        global songs
        songs = [song for song in songs if name != song["name"]]
        return "{} is deleted.".format(name), 200


#api.add_resource(Song, "/user/<string:name>")
api.add_resource(Song, "/users")
app.run(debug=True)


#########################################################################################################


# from flask import Flask
# from flask_restful import Api, Resource, reqparse

# app = Flask(__name__)
# api = Api(app)

# users = [
#     {
#         "name": "Nicholas",
#         "age": 42,
#         "occupation": "Network Engineer"
#     },
#     {
#         "name": "Elvin",
#         "age": 30,
#         "occupation": "Doctor"
#     },
#     {
#         "name": "Jass",
#         "age": 22,
#         "occupation": "Web Developer"
#     }
# ]


# class User(Resource):
#     def get(self, name=None):
#         if name is None:
#             return users, 200
#         for user in users:
#             if name == user["name"]:
#                 return user, 200
#         return "User not Found", 404

#     def post(self, name='Jass'):
#         parser = reqparse.RequestParser()
#         parser.add_argument("age")
#         parser.add_argument("occupation")
#         args = parser.parse_args()

#         for user in users:
#             if name == user["name"]:
#                 return "User with name {} already exists".format(name), 400

#         user = {
#             "name": name,
#             "age": args["age"],
#             "occupation": args["occupation"]
#         }

#         users.append(user)
#         return user, 201

#     def put(self, name='Jass'):
#         parser = reqparse.RequestParser()
#         parser.add_argument("age")
#         parser.add_argument("occupation")
#         args = parser.parse_args()

#         for user in users:
#             if name == user["name"]:
#                 user["age"] = args["age"]
#                 user["occupation"] = args["occupation"]
#                 return user, 200

#         user = {
#             "name": name,
#             "age": args["age"],
#             "occupation": args["occupation"]
#         }

#         users.append(user)
#         return user, 201

#     def delete(self, name='Jass'):
#         global users
#         users = [user for user in users if name != user["name"]]
#         return "{} is deleted.".format(name), 200


# api.add_resource(User, "/user/")
# #api.add_resource(User, "/users")
# app.run(debug=True)
