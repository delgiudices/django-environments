#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of django-environments.
# https://github.com/delgiudices/django-environments

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Luis Del Giudice <luis.dg19@gmail.com>

import os
import shutil

from unittest import TestCase as PythonTestCase

from django_environments import constants


class TestCase(PythonTestCase):

    def setUp(self):
        if os.path.isdir(constants.ENVS_DIR):
            shutil.rmtree(constants.ENVS_DIR)
        else:
            os.mkdir(constants.ENVS_DIR)

    def tearDown(self):
        shutil.rmtree(constants.ENVS_DIR)
