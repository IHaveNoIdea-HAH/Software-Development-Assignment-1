from app.models.user import User

class UserSchema:
    @staticmethod
    def dump(user):
        return {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email
        }

    @staticmethod
    def load(data):
        if 'email' in data:
            email = data['email']
        else:
            email = None

        return User(
            user_id=data.get('id'),
            username=data['username'],
            password=data['password'],
            email=email
        )
