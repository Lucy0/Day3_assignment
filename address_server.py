__author__ = 'Lucy'
"""The Python implementation of the GRPC addressbook.Address server."""

import time

import addressbook_pb2


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Address(addressbook_pb2.EarlyAdopterAddressServicer):
    def __init__(self):
        self.addresses = []

    def AddAddress(self, request, context):
        self.addresses.append(request.person)
        return addressbook_pb2.AddReply(message='Add a person "%s"! ID: %d    Email: %s '
                                                % (request.person.name, request.person.id, request.person.email))
    def DisplayAddress(self, request, context):
        return addressbook_pb2.AddressBook(address = self.addresses)

def serve():
    server = addressbook_pb2.early_adopter_create_Address_server(Address(), 50051, None, None)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
  serve()