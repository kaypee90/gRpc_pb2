import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

import greeter

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response
    
    def Addition(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.addition(
            request.value_one, request.value_two)
        return response

    def Greet(self, request, context):
        response = calculator_pb2.Greeting()
        response.value = greeter.greet(request.name)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

