from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
  readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "request>=2"]

setup(
  name="galileo-notebook",
  version="0.0.2",
  author="Mauricio Feldman-Abe, Jeff Hale",
  author_email="spamme@spepy.net",
  description="A package to convert your Jupyter Notebook",
  long_description=readme,
  long_description_content_type="text/markdown",
  url="https://github.com/mauabe/galileo-notebook",
  packages=find_packages(),
  install_requires=requirements,
  classifiers=[
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  ],
)
