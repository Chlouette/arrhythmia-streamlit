from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='arrhythmia-streamlit',
    #   version="",
      description="package description",
      author="Fab_Lu_Chlo",
      url="https://github.com/Chlouette/arrhythmia-streamlit",
      packages=find_packages(), # NEW: find packages automatically
      install_requires=requirements)
