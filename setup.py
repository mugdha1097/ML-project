from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements

setup(
name='mlproject',
version='0.0.1',
author='Mugdha',
author_email='mugdhamirashi19@gmail.com',
package=find_packages(),
install_requires=get_requirements('requirements.txt'),
)