# See:
#
#     https://pypi.python.org/pypi/virtualenv
#
# and:
#
#     http://s3.pixane.com/pip_distribute.png
#
# and:
#
#     http://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python


# Select current version of virtualenv:
VERSION=1.9.1
# Name your first "bootstrap" environment:
INITIAL_ENV=py-env0
# Options for your first environment:
ENV_OPTS='--distribute'
# Set to whatever python interpreter you want for your first environment:
PYTHON=$(which python27)
# Where to get virtualenv from:
URL_BASE=http://pypi.python.org/packages/source/v/virtualenv



# --- Real work starts here ---
curl -O $URL_BASE/virtualenv-$VERSION.tar.gz
tar xzf virtualenv-$VERSION.tar.gz
# Create the first "bootstrap" environment.
$PYTHON virtualenv-$VERSION/virtualenv.py $ENV_OPTS $INITIAL_ENV
# Don't need this anymore.
rm -rf virtualenv-$VERSION
# Install virtualenv into the environment.
$INITIAL_ENV/bin/pip install virtualenv-$VERSION.tar.gz
# Remove virtualenv package. No need to leave this around if we spawn
# environments from our original bootstrap.
rm virtualenv-$VERSION.tar.gz
# Create a virtualenv for the class.
$INITIAL_ENV/bin/virtualenv $ENV_OPTS py-class

# And then to switch to the environment:
#
#     source py-class/bin/activate
#
# This will give us pip and distribute by.
# And to get out:
#
#     deactivate
#
