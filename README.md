# TP-VulnBox

<p align="center">
	<a href="https://github.com/truocphan/TP-VulnBox/releases/"><img src="https://img.shields.io/github/release/truocphan/TP-VulnBox" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/downloads/truocphan/TP-VulnBox/total" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/stars/truocphan/TP-VulnBox" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/forks/truocphan/TP-VulnBox" height=30></a>
	<a href="https://github.com/truocphan/TP-VulnBox/issues?q=is%3Aopen+is%3Aissue"><img src="https://img.shields.io/github/issues/truocphan/TP-VulnBox" height=30></a>
	<a href="https://github.com/truocphan/TP-VulnBox/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/truocphan/TP-VulnBox" height=30></a>
	<a href="https://pypi.org/project/TP-VulnBox/" target="_blank"><img src="https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" height=30></a>
	<a href="https://www.facebook.com/61550595106970" target="_blank"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" height=30></a>
	<a href="https://twitter.com/TPCyberSec" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" height=30></a>
	<a href="https://github.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height=30></a>
	<a href="mailto:tpcybersec2023@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" height=30></a>
	<a href="https://www.buymeacoffee.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" height=30></a>
</p>

## Installation
#### From PyPI:
```console
pip install TP-VulnBox
```
#### From Source:
```console
git clone https://github.com/truocphan/TP-VulnBox.git --branch <Branch/Tag>
cd TP-VulnBox
python setup.py build
python setup.py install
```

## Basic Usage
```
> TP-VulnBox --help

 ____   ____        __            ______
|_  _| |_  _|      [  |          |_   _ \
  \ \   / /__   _   | |  _ .--.    | |_) |   .--.   _   __
   \ \ / /[  | | |  | | [ `.-. |   |  __'. / .'`\ \[ \ [  ]
    \ ' /  | \_/ |, | |  | | | |  _| |__) || \__. | > '  <
     \_/   '.__.'_/[___][___||__]|_______/  '.__.' [__]`\_]


usage: TP-VulnBox [-h] [--list-all] [--start VulnBox_NAME] [--run VulnBox_NAME] [--delete VulnBox_NAME] [--update] [--version]

options:
  -h, --help            show this help message and exit
  --list-all            Lists all available VulnBoxes
  --start VulnBox_NAME  Download and run the new VulnBox (e.g. CVE-2024-31211)
  --run VulnBox_NAME    Run an existing VulnBox or run a new VulnBox if not already downloaded (e.g. CVE-2024-31211)
  --delete VulnBox_NAME
                        Delete downloaded VulnBox (e.g. CVE-2024-31211)
  --update              Update TP-VulnBox to the latest version
  --version             Print the current version of TP-VulnBox

VulnBox is a container that is intentionally designed with vulnerabilities to allow security professionals to practice and improve their
offensive security skills, such as penetration testing and vulnerability assessment.

```
