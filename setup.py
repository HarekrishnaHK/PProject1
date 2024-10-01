from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[],
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

    setup (
    name ="PProject1",
    version="0.0.1",
    author="Harekrishna",
    author_email="adhikaryharekrishna80@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt")

)
