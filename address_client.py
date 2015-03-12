__author__ = 'Lucy'
"""The Python implementation of the GRPC addressbook.Address client."""

import addressbook_pb2

_TIMEOUT_SECONDS = 10

def addperson(stub, name, id, email):
    stub.person = addressbook_pb2.Person()
    stub.person.name = name
    stub.person.id = id
    stub.person.email = email
    response = stub.AddAddress(addressbook_pb2.AddRequest(person = stub.person), _TIMEOUT_SECONDS)
    print(response.message)

def run():
    with addressbook_pb2.early_adopter_create_Address_stub('localhost', 50051) as stub:
        addperson(stub, 'Lucy', 123456, 'lucy@gmail.com')
        addperson(stub, 'Daire', 123457, 'daire@gmail.com')

        print("Display address book:")
        response = stub.DisplayAddress(addressbook_pb2.DisplayRequest(), _TIMEOUT_SECONDS)
        for address in response.address:
            print('Name %s   ID: %d    Email: %s' % (address.name, address.id, address.email))

if __name__ == '__main__':
    run()