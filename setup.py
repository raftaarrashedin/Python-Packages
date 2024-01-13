from setuptools import setup, find_packages
from typing import List


with open('README.md','r', encoding = 'utf-8') as f:

	long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Python-Packages"
PKG_NAME = "databaseautomation"
AUTHOR_USER_NAME = "raftaarrashedin"
AUTHOR_EMAIL = "raftaarrashedin100@gmail.com"
https://github.com/raftaarrashedin
setup(
	name = PKG_NAME,
	version = __version__,
	author = AUTHOR_USER_NAME,
	author_email = AUTHOR_EMAIL,
	description = "A python package for connecting with database.",
	long_description = long_description,
	long_description_content = "text/markdown",
	url = f"https://github.com/{AUTHOR_USER_NAME}/{Python-Packages}",
	project_urls = {
		"Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{Python-Packages}/issues",
	},
	package_dir = {"": "src"},
	packages = find_packages(where="src")
)