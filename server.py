import argparse
import logging
import threading

import zmq

import core
import service


logger = logging.getLogger(__name__)


class Worker(core.Worker):
    def __init__(self, i, *args, **kw):
        super(Worker, self).__init__(*args, **kw)
        self.i = i

    def call_method(self, method, b_input):
        print("Worker %s handles a %r call" % (self.i, method.name))
        return super(Worker, self).call_method(method, b_input)


def worker_job(url, i, ctx):
    logging.basicConfig()
    worker = Worker(i, service.DummyService(), url, ctx)
    worker.run()


def main():
    logging.basicConfig()

    parser = argparse.ArgumentParser(description='Launch server.')
    parser.add_argument('-n', type=int, default=2, help="How many worker shall we use?")
    parser.add_argument('--bind', '-b', type=str, default="tcp://*:8787", help="bind? default: tcp://*:8787")

    args = parser.parse_args()

    n_workers = args.n
    url = args.bind

    ctx = zmq.Context()

    broker = core.Broker(url, 'inproc://workers', ctx)

    worker_jobs = []
    for i in range(n_workers):
        worker_jobs.append(threading.Thread(target=worker_job, args=('inproc://workers', i, ctx)))
        worker_jobs[-1].daemon = True
        worker_jobs[-1].start()

    print("Waiting on %r" % url)
    broker.run()


if __name__ == '__main__':
    main()
