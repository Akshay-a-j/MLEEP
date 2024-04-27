from setuptools import find_packages, setup
from typing import List

hypen_dot_e = "-e ."

def get_requirements(file_path:str)->List[str]:

    requirements = []
    with open(file_path) as f_out:
        requirements = f_out.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)

    return requirements


setup(
name="mlprojects",
version="0.0.1",
author="Akshay",
author_email="akshay.jagajampi2@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)