import zmq

class ZmqPublisher:
    
    def __init__(self):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.connect("tcp://localhost:5555")

    def publish(self, message: dict):
        self.__socket.send_string(message)
