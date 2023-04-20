import zmq

class ZmqPublisher:
    
    def __init__(self):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.PUB)
        self.__socket.bind("tcp://127.0.0.1:5555")

    def publish(self, message: dict):
        self.__socket.send_json(message)
