import sys

from .env import Env


def new(name, out=sys.stdout):
    Env(name).create()
    out.write('Environment \'{0}\' was created.'.format(name))


def list(out=sys.stdout):
    out.write('Created environments:')
    for env in Env.all():
        out.write('- {0}'.format(env))
