class User:
    def __init__(self, user_id, username, password, email=None):
        self.id = user_id  # Unique identifier for the user
        self.username = username  # Username of the user
        self.password = password  # In production, store hashed passwords!
        self.email = email  # Optional email field

