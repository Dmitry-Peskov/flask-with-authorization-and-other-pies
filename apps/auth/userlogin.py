from .controler import get_user_by_email


class UserLogin:


    def from_db(self, user_email: str):
        self.__user = get_user_by_email(user_email)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return self.__user is not None

    def is_active(self):
        return self.__user.active

    def is_anonymous(self):
        return self.__user is None

    def get_id(self):
        return self.__user.email