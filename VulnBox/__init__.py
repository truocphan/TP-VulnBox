import argparse
import requests
import os
from io import BytesIO
import zipfile


def List_All_VulnBox():
	try:
		print("\x1b[32m[*] List of all available VulnBoxes:\x1b[0m")
		res = requests.get("https://api.github.com/repos/truocphan/VulnBox/releases").json()
		for release in res:
			print("- \x1b[1;35m" + release["name"].split(":",1)[0] + "\x1b[1;0m:" + release["name"].split(":",1)[1])
	except Exception as e:
		pass
	print("")


def start_VulnBox(VulnBox_NAME):
	BoxComposeFile = os.path.join(VulnBoxDir, VulnBox_NAME, "docker-compose.yaml")

	if not os.path.isfile(BoxComposeFile):
		try:
			# Download and extract the VulnBox file
			with zipfile.ZipFile(BytesIO(requests.get("https://github.com/truocphan/VulnBox/releases/download/"+VulnBox_NAME+"/"+VulnBox_NAME+".zip").content)) as zipObject: zipObject.extractall(path=VulnBoxDir)
		except zipfile.BadZipfile:
			exit("\x1b[1;31m[-] The \""+VulnBox_NAME+"\" is not available at VulnBox.\x1b[1;0m")
		except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout):
			exit("\x1b[1;31m[-] Network connection problem. Please check your network connection and try again.\x1b[1;0m")

	try:
		# Start VulnBox
		os.system("docker-compose -f "+BoxComposeFile+" up")
	except KeyboardInterrupt:
		# Stop VulnBox and clear volumn
		os.system("docker-compose -f "+BoxComposeFile+" down -v")


def main():
	global VulnBoxDir
	VulnBoxDir = os.path.join(os.path.expanduser("~"), "PyPI-VulnBox")
	if not os.path.isdir(VulnBoxDir): os.mkdir(VulnBoxDir)

	print("\x1b[1;31m"+r"""
 ____   ____        __            ______
|_  _| |_  _|      [  |          |_   _ \
  \ \   / /__   _   | |  _ .--.    | |_) |   .--.   _   __
   \ \ / /[  | | |  | | [ `.-. |   |  __'. / .'`\ \[ \ [  ]
    \ ' /  | \_/ |, | |  | | | |  _| |__) || \__. | > '  <
     \_/   '.__.'_/[___][___||__]|_______/  '.__.' [__]`\_]
                                                           
"""+"\x1b[1;0m")

	parser = argparse.ArgumentParser(prog="TP-VulnBox",
		epilog="\x1b[1;33mVulnBox is a container that is intentionally designed with vulnerabilities to allow security professionals to practice and improve their offensive security skills, such as penetration testing and vulnerability assessment.\x1b[1;0m")
	parser.add_argument("--list-all", action="store_true", help="Lists all available VulnBoxes")
	parser.add_argument("--start-VulnBox", metavar="VulnBox_NAME", type=str, help="Run the new VulnBox (e.g. CVE-2023-51412)")
	args = parser.parse_args()

	if args.list_all:
		List_All_VulnBox()
	elif args.start_VulnBox:
		start_VulnBox(args.start_VulnBox)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()