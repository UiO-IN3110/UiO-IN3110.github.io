from setuptools import setup

setup(name = 'pkg',
      version = '0.1',
      description = 'Simple package',
      author = 'Miroslav Kuchta',
      author_email = 'miroslav.kuchta@gmail.com',
      # url = 'https://github.com/mirok/...',
      packages = ['pkg'],
      package_dir = {'pkg': 'pkg'}
)
