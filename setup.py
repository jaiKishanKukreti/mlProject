from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Add parentheses to call the method
        requirements = [req.strip() for req in requirements]  # Use .strip() to remove whitespace, including newline
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements



setup(
    name='mlProject',
    version='0.0.1',
    author='JAIKISHAN',
    author_email='jaikishan93@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)