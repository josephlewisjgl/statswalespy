import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


setup(
  name = 'statswalespy',
  packages = ['statswalespy'],
  version = '0.1.0',
  license='MIT',
  description = 'A Python package for downloading data and metadata from the StatsWales API.',
  author = 'Joe Lewis, Jamie Ralph',
  author_email = 'josephgeorgelewis2000@gmail.com',
  long_description=README,
  long_description_content_type="text/markdown",
  url = 'https://github.com/josephlewisjgl/statswalespy',
  keywords = ['Wales', 'statswales', 'Welsh'],
  install_requires=[
          'logging',
          'pandas',
          'requests'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
