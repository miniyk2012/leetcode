import user


class Comment:
    def __init__(self, user_id):
        self._user_id = user_id

    def get_user(self) -> 'user.User':
        return user.User(self._user_id)

