import core
from gen import message_pb2 as gen


USER_NAMES = ["Batman", "toto", "Superman", "Spiderman"]
USERS = [gen.User(name=name) for name in USER_NAMES]


def echo(req):
    rep = gen.EchoResponse()
    rep.echo = req.echo
    return rep


def add(req):
    rep = gen.AddResponse()
    rep.result = req.a + req.b
    return rep


def search(req):
    rep = gen.SearchResponse()
    rep.users.extend(filter(lambda x: req.query.lower() in x.name.lower(), USERS))
    return rep


class DummyService(core.ServiceDefinition):
    def __init__(self):
        super(DummyService, self).__init__("DummyService", {})
        self.methods['echo'] = core.Method('echo', gen.EchoRequest, gen.EchoResponse, echo)
        self.methods['add'] = core.Method('add', gen.AddRequest, gen.AddResponse, add)
        self.methods['search'] = core.Method('search', gen.SearchRequest, gen.SearchResponse, search)
