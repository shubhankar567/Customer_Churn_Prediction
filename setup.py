from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
    requirements = [requirement.replace('\n', '') for requirement in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')

setup(
    name='src',
    version = '0.0.1',
    author='Shubhankar Chaturvedi',
    author_email='shubhankar5848@gmail.com',
    packages=find_packages(),
    install_here = get_requirements('requirements.txt')
)