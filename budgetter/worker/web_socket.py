from PySide6.QtCore import QObject, QUrl
from PySide6.QtWebSockets import QWebSocket


class WebSocketClient(QObject):
    """
    Web socket client implementation
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Store function, arguments and result
        self._client = QWebSocket()

        # Connect all slots and signals
        self.connect_slots_and_signals()

        # Open URL
        self._client.open(QUrl("ws://127.0.0.1:8080/ws/dashboard/"))

    def connect_slots_and_signals(self):
        """
        Connect slots from ws client

        :return: None
        """

        self._client.connected.connect(self.on_connect)
        self._client.disconnected.connect(self.closed)

    def on_connect(self):
        """
        Callback from connection

        :return: None
        """

        self._client.textMessageReceived.connect(self.on_received)
        self._client.binaryMessageReceived.connect(self.on_received)

    def on_received(self, message):
        """
        Callback when message received

        :param message: message received
        :return: None
        """

        print(message)

    def closed(self):
        """
        Callback when disconnected

        :return: None
        """

        self._client.close()
