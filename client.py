import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

number = calculator_pb2.Number(value=16)
response = stub.SquareRoot(number)
print(response.value)

more_numbers = calculator_pb2.MoreNumbers(
                    value_one=16, value_two=4)
response_two = stub.Addition(more_numbers)
print(response_two.value)

person = calculator_pb2.Person(name="Kwabena")
response_three = stub.Greet(person)
print(response_three.value)