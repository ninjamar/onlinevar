from distutils.core import setup
setup(
  name = 'onlinevar',
  author_email = 'example@example.com',
  version = '0.1.0',
  classifiers = [
      "Programming Language :: Python :: 3",
  ],
  description = 'online vars in python',
  licence = 'MIT',
  instal_requires =['requests','json','os','https.server','socketserver','socket'],
  packages = ['onlinevar'],
  author = 'ninjamar',
  python_require = '>=3.7',
  url = 'https://github.com/ninjamar/onlinevar'
)
