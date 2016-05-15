import sys

ENVS_DIR = 'envs'
TEMPLATES = (
    'nginx.conf',
)

# Test Constants

if 'nose' in sys.modules.keys():
    ENVS_DIR = 'test_envs'
