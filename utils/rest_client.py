import requests
import json

from PySide2.QtCore import QThread


class Thread(QThread):
    """
    Thread to run specific function
    """

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)

        """ Store function, arguments and result """
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

    @staticmethod
    def POST(url, data):
        """
        Post method
        :param url: url
        :param data: data to push - JSON format
        :return: JSON return
        """

        """ Call post method """
        response = requests.post(url, json=data)

        """ Handle error case """
        if response.status_code != 201:
            raise Exception('[ERROR] GET {response.url} return code: {response.status_code}'
                            '\ndata: {response.json}'.format(response=response))

        return response.json()

    @staticmethod
    def GET(url):
        """
        Get method
        :param url: url
        :return: JSON return
        """

        """ Call get method """
        response = requests.get(url)

        """ Handle error case """
        if response.status_code != 200:
            raise Exception('[ERROR] POST {response.url} return code: {response.status_code}'
                            '\ndata: {response.json}'.format(response=response))

        return response.json()

    @staticmethod
    def DELETE(url):
        """
        Delete method
        :param url: url
        :return: JSON return
        """

        """ Call delete method """
        response = requests.delete(url)

        """ Handle error case """
        if response.status_code != 200:
            raise Exception('[ERROR] DELETE {response.url} return code: {response.status_code}'
                            '\ndata: {response.json}'.format(response=response))

        return response.json()
