from setuptools import setup, find_packages

NAME = 'kaviyesutil'
VERSION = '2.0.0'
DESCRIPTION = "A standard kaviyes utility for python thats ideal for small projects and prototypes."
AUTHOR = 'Kaviyes'
AUTHOR_EMAIL = 'kaviyeslabs@proton.me'
URL = 'https://github.com/Kaviyes/kaviyesutil'
LICENSE = 'MIT'

with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    package_data={
        '': ['LICENSE']
    },
    packages=find_packages(),
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
    install_requires=[ ],
    python_requires='>=3.10',
)
