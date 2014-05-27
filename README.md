poc-pzmq
========

RPC with ZMQ + protobuf


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
