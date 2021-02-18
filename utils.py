import requests
import json


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
        if response.status_code != 200:
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
