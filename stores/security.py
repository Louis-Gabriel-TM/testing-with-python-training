from werkzeung.security import safe_str_cmp

from models.user import UserModel


def authenticate(username, password):
    """
    Function that gets called when a user calls the /auth endpoint
    with thier username and password.
    :param username: User's username in string format.
    :param password: User's un-encrypted password in string format.
    :return: a UserModel object if authenticate was successful, None otherwise.
    """
    user = UserModel.find_by_username(username)

    if user and safe_str_cmp(user.password, password):
        return user


def identify(payload):
    """
    Function that gets called when user has already authenticate, and Flask-JWT
    verified their authorization header is correct.
    :param payload: a dictionary with 'identity' key, which is the user id..
    :return: a UserModel object.
    """
    user_id = payload['identity']

    return UserModel.find_by_id(user_id)
