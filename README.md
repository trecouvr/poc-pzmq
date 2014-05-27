poc-pzmq
========

RPC with ZMQ + protobuf
Multiple clients may connect to a single endpoint to access a service, the request is then
dispatched to a pool of workers. More details on http://zguide.zeromq.org/page:all#Shared-Queue-DEALER-and-ROUTER-sockets.


Installation
------------

    pip install -r requirements.txt


Run server
----------

    python server.py
    # get some help
    python server.py --help


Run client
----------

    python client.py
    # get some help
    python client.py --help


Compile *.proto
---------------

    protoc --python_out=gen message.proto
