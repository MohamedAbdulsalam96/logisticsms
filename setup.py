# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in logisticsms/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('logisticsms/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='logisticsms',
	version=version,
	description='This system is for a logistics company to import, clear, store and dispatch the goods for customers.',
	author='Aakvatech Limited',
	author_email='info@aakvatech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
