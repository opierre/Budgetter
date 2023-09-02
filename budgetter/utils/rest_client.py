import requests

from PySide6.QtCore import QThread


class Thread(QThread):
    """
    Thread to run specific function
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store function, arguments and result
        self.function = None
        self.arguments = None
        self.result = None

    def set_function(self, function, args):
        """
        Setter for function and arguments

        :param function: function
        :param args: arguments
        :return: None
        """

        self.function = function
        self.arguments = args

    def run(self):
        """
        Override run function from QThread
        :return: None
        """

        self.result = self.function(*self.arguments)


class RestClient:
    """
    Rest Client API
    """

    # Store session
    # session = requests.Session()

    @staticmethod
    def post(url, data):
        """
        Post method

        :param url: url
        :param data: data to push - JSON format
        :return: JSON return
        """

        # Call post method
        response = requests.post(url, json=data, timeout=2.5)

        # Handle error case
        if response.status_code != 201:
            raise BackEndError(response)

        return response.json()

    @staticmethod
    def get(url) -> dict:
        """
        Get method

        :param url: url
        :return: JSON return
        """

        # Call get method
        response = requests.get(url, timeout=3.5)

        # Handle error case
        if response.status_code != 200:
            raise BackEndError(response)

        return response.json()

    @staticmethod
    def delete(url) -> dict:
        """
        Delete method

        :param url: url
        :return: JSON return
        """

        # Call delete method
        response = requests.delete(url, timeout=1.5)

        # Handle error case
        if response.status_code not in {200, 204}:
            raise BackEndError(response)

        return {}

    @staticmethod
    def patch(url, data):
        """
        Patch method

        :param url: url
        :param data: data to patch - JSON format
        :return: JSON return
        """

        # Call post method
        response = requests.patch(url, json=data, timeout=2.5)

        # Handle error case
        if response.status_code != 200:
            raise BackEndError(response)

        return response.json()


class BackEndError(Exception):
    """
    Exception for handling back end errors from server
    """

    def __init__(self, response: requests.Response):
        self.status_code = response.status_code
        self.error_msg = (f"Backend server return status code {self.status_code} for current access: {response.url}\n"
                          f"{response.text}")

    def __str__(self):
        return self.error_msg
