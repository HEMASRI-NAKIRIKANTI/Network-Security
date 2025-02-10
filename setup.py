from setuptools import setup, find_packages
from typing import List

DASH_E_DOT ='-e .'
def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
      with open('requirements.txt','r') as file:
        lines = file.readlines()
        for line in lines:
           requirement =line.strip()
           if requirement and requirement!=DASH_E_DOT:
              requirements_lst.append(requirement)
      return requirements_lst
    except FileNotFoundError:
       print("requirement.txt is not found")

             
get_requirements()

setup(
   name="NetworkSecurity",
   version='0.0.1',
   author='Hema Sri Nakirikanti',
   author_email='hnakirik@ttu.edu',
   packages=find_packages(),
   install_requires =get_requirements()
)

