Implementation example
======================


This simple example show how to expose a service with 3 methods: ``echo``, ``add`` and ``search``
via pzmq.


Run server::

    python server.py
    # get some help
    python server.py --help


Run client::

    python client.py
    # get some help
    python client.py --help


Compile proto files::

    protoc --python_out=gen message.proto
