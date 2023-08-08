from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def get(self, user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return {'message': 'User not found'}, 404

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        args = parser.parse_args() 
        user = {'id': user_id, 'name': args['name'], 'email': args['email']}
        users.append(user)
        return user, 201

@app.route('/form', methods=['GET'])
def user_form():
    return render_template('user_form.html', user_id=0) 
api.add_resource(User, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
