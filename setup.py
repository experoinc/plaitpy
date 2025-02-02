from distutils.core import setup
import re, io

VERSION = re.search(
    r'VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('src/version.py', encoding='utf_8_sig').read()
).group(1)

setup(
    name='plaitpy',
    version=VERSION,
    author='okay',
    author_email='okay.zed+pltpy@gmail.com',
    packages=['plaitpy' ],
    package_dir={ 'plaitpy': 'src' },
    scripts=['bin/plait.py'],
    package_data={'plaitpy': [
        '../README.md',
        './*',
        '../templates/*/*',
        '../vendor/faker/lib/locales/*/*.yml',
        '../vendor/faker/lib/locales/*.yml',
    ]},
    url='http://github.com/plaitpy/plaitpy',
    license='MIT',
    description='a fake data generator',
    long_description=open('README.md').read(),
    install_requires=[
        "pyyaml~=5.0"
    ],
    )
