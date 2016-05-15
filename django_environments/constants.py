import sys

ENVS_DIR = 'envs'

# Test Constants

if 'nose' in sys.modules.keys():
    ENVS_DIR = 'test_envs'
