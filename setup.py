from setuptools import setup
import wise_utils

setup(name='python-wise-utils',
      version=wise_untils.__version__,
      py_modules=['wise_utils'],
      author='@wisdomwolf',
      author_email='wisdomwolf@gmail.com',
      install_requires=[
          'PyYAML==5.3'
      ],
)
