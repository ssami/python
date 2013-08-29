import os
from fabric.api import env


# Where is this file located at?
cwd = os.path.realpath(os.path.dirname(__file__))

# whoami
env.user = "student4"
# List of hosts to run against.
env.hosts = [
    'ec2-107-21-80-136.compute-1.amazonaws.com',
]
# Location of our keyfile.
env.key_filename = os.path.join(cwd, "student")
