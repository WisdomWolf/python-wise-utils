from setuptools import setup
import wise_utils

setup(name='python_wise_utils',
      version=wise_utils.__version__,
      packages=setuptools.find_packages(),
      author='@wisdomwolf',
      author_email='wisdomwolf@gmail.com',
      install_requires=[
          'PyYAML==5.3'
      ],
)
