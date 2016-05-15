import os

from StringIO import StringIO

from django_environments import commands, constants
from tests.base import TestCase


class CreateTestCase(TestCase):

    def test_environment_is_created(self):
        name = 'production'
        out = StringIO()
        self.assertFalse(os.path.isdir(os.path.join(constants.ENVS_DIR, name)))
        commands.new(name, out=out)
        output = out.getvalue().strip()
        self.assertEqual(
            output, 'Environment \'{0}\' was created.'.format(name)
        )
        self.assertTrue(os.path.isdir(os.path.join(constants.ENVS_DIR, name)))

    def test_error_raised_if_environment_exists(self):
        name = 'production'
        commands.new(name)
        with self.assertRaises(Exception):
            commands.new(name)


class ListTestCase(TestCase):

    def test_listing_created_environments(self):
        name = 'production'
        out = StringIO()
        commands.new(name, out=StringIO())
        commands.list(out=out)
        output = out.getvalue().strip()
        self.assertTrue(name in output)
