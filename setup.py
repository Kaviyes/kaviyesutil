import io
import os
import pathlib

import setuptools

package_root = pathlib.Path(__file__).parent.resolve()

NAME = 'kaviyesutil'
VERSION = '2.1.2'
DESCRIPTION = "A standard kaviyes utility for python thats ideal for small projects and prototypes."
AUTHOR = 'Kaviyes'
AUTHOR_EMAIL = 'contact.karlvince@gmail.com'
URL = 'https://github.com/Kaviyes/kaviyesutil'
LICENSE = 'MIT'
README = (package_root / "README.md").read_text()

packages = [
    package for package in setuptools.PEP420PackageFinder.find() if package.startswith("kaviyes")
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    package_data={
        '': ['LICENSE']
    },
    packages=packages,
    keywords=['utility', 'toolkit'],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',  
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
    install_requires=["requests"],
    python_requires='>=3.9',
)