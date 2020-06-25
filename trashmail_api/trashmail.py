import requests
import hashlib


class TrashMail:

    def __init__(self, token):
        """
        Initialization of object
        :param token:
        """
        self.base = "https://trashmail-api.de/api/v1/{endpoint}"
        self.token = token
        self.header = {
            "Content-Type": 'application/json',
            "Authorization": 'Bearer {}'.format(self.token),
            "Accept": 'application/json'
        }

    @staticmethod
    def get_params_filter(filter):
        """
        Returns the params for get requests
        :param filter:
        :return:
        """

        return {
            "status": filter
        }

    def check_mail(self, email, md5=False):
        """
        Function to check the provided mail
        :param md5: optional parameter to check host instead of email directly (General Data Protection Regulation GDPR)
        :param email: email to check
        :return: json (from api)
        """

        if md5:
            params = {
                "host": hashlib.md5(email)
            }
        else:
            params = {
                "input": email
            }

        r = requests.get(self.base.format(endpoint="check"), params=params, headers=self.header)

        return r.json()

    def add_mails(self, items=[], status="private", regular=True):
        """
        Adds e-mail hosts to the trashmail database
        PLEASE NOTE: AS A REGULAR USER, YOU CANNOT SET ANY STATUS
        :param regular: Change to False, if you have higher ranking
        :param items: array of all mails
        :param status: YOU CAN CHOOSE BETWEEN: whitelisted, public, private !! OPTIONAL
        :return:
        """

        if regular:
            params = {
                "items": items
            }
        else:
            params = {
                "items": items,
                "status": status
            }

        r = requests.post(self.base.format(endpoint="trashmail/add"), params=params, headers=self.header)

        return r.json()

    def me(self):
        """
        Fetches all information regarding your account on trashmail-api.de
        :return:
        """
        r = requests.get(self.base.format(endpoint="me"), headers=self.header)

        return r.json()

    def get_list(self, filter=None):
        """
        Fetches the Lists you want
        :param filter: Filter : OPTIONAL || None, private, public, whitelisted
        :return:
        """

        if filter is not None:
            params = self.get_params_filter(filter)
        else:
            params = {}

        r = requests.get(self.base.format(endpoint="trashmail/list"), params=params, headers=self.header)

        return r.json()

    def get_count(self):
        """
        Fetches current statistics for trashmail-api.de
        :return:
        """
        r = requests.get(self.base.format(endpoint="trashmail/count"), headers=self.header)

        return r.json()

    def change_account_settings(self, logging=True, anonymize=True):
        """
        Changes your account settings regarding anonymizing and requests logging
        :param logging: set to True or False
        :param anonymize: set to True or False
        :return:
        """

        r = requests.post(self.base.format(endpoint="me"), params={
            "logging": logging,
            "anonymize": anonymize
        }, headers=self.header)

        return r.json()

