from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(filename:str)->List[str]:
    """
    This function will return the list of requirements.
    """
    with open(filename, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="END TO END ML PROJECT",
    version="0.0.1",
    author="Ologundudu Fareed",
    author_email="ologundudufareed@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)