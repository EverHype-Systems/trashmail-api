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

