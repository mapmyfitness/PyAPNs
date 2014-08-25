from distutils.core import setup
import sys

version = "1.2.1"

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version(version, __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()


setup(
    author = 'Simon Whitaker',
    author_email = 'simon@goosoftware.co.uk',
    description = 'A python library for interacting with the Apple Push Notification Service',
    download_url = 'http://github.com/simonwhitaker/PyAPNs',
    license = 'unlicense.org',
    name = 'apns',
    py_modules = ['apns'],
    scripts = ['apns-send'],
    url = 'http://www.goosoftware.co.uk/',
    version = version,
)
