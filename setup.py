# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hr_customization/__init__.py
from hr_customization import __version__ as version

setup(
	name='hr_customization',
	version=version,
	description='HR Module Related Customization',
	author='Jigar Tarpara',
	author_email='team@khatavahi.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
