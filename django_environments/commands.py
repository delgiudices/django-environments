from .env import Env


def new(name):
    Env(name).create()
    print 'Environment \'{0}\' was created.'.format(name)


def list():
    print 'Created environments:'
    for env in Env.all():
        print '- {0}'.format(env)
