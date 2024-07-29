import setuptools

setuptools.setup(
	name = "TP-VulnBox",
	version = "2024.7.29",
	author = "TP Cyber Security",
	license = "MIT",
	author_email = "tpcybersec2023@gmail.com",
	description = "VulnBox is a container that is intentionally designed with vulnerabilities to allow security professionals to practice and improve their offensive security skills, such as penetration testing and vulnerability assessment.",
	long_description = open("README.md").read(),
	long_description_content_type = "text/markdown",
	install_requires = open("requirements.txt").read().split(),
	url = "https://github.com/truocphan/TP-VulnBox",
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
	],
	entry_points = {
		"console_scripts": [
			"TP-VulnBox = VulnBox:main"
		]
	},
)