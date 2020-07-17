from setuptools import setup
import re

with open('src/enzo/__init__.py', encoding='utf8') as f:
    version = re.search(R"__version__ = '(.*?)'", f.read()).group(1)


# Metadata in setup.cfg
setup(
    install_requires=[
        'numpy==1.19.0',
    ],
    version=version,
)
