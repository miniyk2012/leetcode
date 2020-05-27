"""Overriding user's model example."""

import dependency_injector.providers as providers


class User:
    """Example class User."""

    def __init__(self, id, password):
        """Initialize instance."""
        self.id = id
        self.password = password
        super().__init__()


class UsersService:
    """Example class UsersService."""

    def __init__(self, user_cls):
        """Initialize instance."""
        self.user_cls = user_cls
        super().__init__()

    def get_by_id(self, id):
        """Find user by his id and return user model."""
        return self.user_cls(id=id, password='secret' + str(id))


# Users factory and UsersService provider:
users_service = providers.Factory(UsersService, user_cls=User)

# Getting several users and making some asserts:
user1 = users_service().get_by_id(1)
user2 = users_service().get_by_id(2)

assert isinstance(user1, User)
assert user1.id == 1
assert user1.password == 'secret1'

assert isinstance(user2, User)
assert user2.id == 2
assert user2.password == 'secret2'

assert user1 is not user2

# Extending user model and user service for adding custom attributes without
# making any changes to client's code.


class ExtendedUser(User):
    """Example class ExtendedUser."""

    def __init__(self, id, password, first_name=None, last_name=None,
                 gender=None):
        """Initialize instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        super().__init__(id, password)


class ExtendedUsersService(UsersService):
    """Example class ExtendedUsersService."""

    def get_by_id(self, id):
        """Find user by his id and return user model."""
        user = super(ExtendedUsersService, self).get_by_id(id)
        user.first_name = 'John' + str(id)
        user.last_name = 'Smith' + str(id)
        user.gender = 'male'
        return user


# Overriding users_service provider:
extended_users_service = providers.Factory(ExtendedUsersService,
                                           user_cls=ExtendedUser)
users_service.override(extended_users_service)

# Getting few other users users and making some asserts:
user3 = users_service().get_by_id(3)
user4 = users_service().get_by_id(4)

assert isinstance(user3, ExtendedUser)
assert user3.id == 3
assert user3.password == 'secret3'
assert user3.first_name == 'John3'
assert user3.last_name == 'Smith3'

assert isinstance(user4, ExtendedUser)
assert user4.id == 4
assert user4.password == 'secret4'
assert user4.first_name == 'John4'
assert user4.last_name == 'Smith4'

assert user3 is not user4