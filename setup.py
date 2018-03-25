from setuptools import setup

setup(
	name='cryptosite',
	packages=['cryptosite'],
	include_package_data=True,
	install_requires=[
		'flask',
		'pymongo',
	],
	setup_requires=[
		'pytest-runner',
	],
	tests_require=[
		'pytest',
	],
)
