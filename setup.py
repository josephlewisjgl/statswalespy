from distutils.core import setup


setup(
  name = 'statswalespy',
  packages = ['statswalespy'],
  version = '0.1',
  license='',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The statswalespy package can be used to retrieve data from the StatsWales API into a Pandas dataframe',   # Give a short description about your library
  author = 'Joe Lewis',
  author_email = 'josephgeorgelewis2000@gmail.com',
  url = 'https://github.com/josephlewisjgl/statswalespy',
  download_url = 'https://github.com/josephlewisjgl/statswalespy/archive/refs/tags/v0.1-beta.tar.gz',    # I explain this later on
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
    'License :: OSI Approved ::  License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)