from setuptools import setup

setup(
    name= 'pythonPackDemo',
    version ='0.0.1',
    packages =['myhellolib'],
    install_requires=[
      'requests',
      'importlib; python_version == "3.8"',
   ],
)