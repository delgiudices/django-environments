import os

from . import constants


class Env(object):

    @classmethod
    def all(cls):
        dirs = os.listdir(constants.ENVS_DIR)
        return [entry for entry in dirs if Env(entry).exists]

    def __init__(self, name):
        self.name = name

    def create(self):
        if self.exists:
            raise Exception(
                'Environment \'{0}\' already exists'.format(self.name)
            )
        if not os.path.isdir(constants.ENVS_DIR):
            os.mkdir(constants.ENVS_DIR)

        os.mkdir(self.path)

    @property
    def exists(self):
        return os.path.isdir(self.path)

    @property
    def path(self):
        return '{0}/{1}'.format(constants.ENVS_DIR, self.name)
