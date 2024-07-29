import argparse
import requests
import os, sys, subprocess, shutil
import re
from io import BytesIO
import zipfile
from tqdm import tqdm


def download_and_extract_zip(VulnBox_NAME, VulnBoxDir):
	url = "https://github.com/truocphan/"+("TP-VulnBox" if VulnBox_NAME == "WP-XDEBUG" else "VulnBox")+"/releases/download/"+VulnBox_NAME+"/"+VulnBox_NAME+".zip"

	response = requests.get(url, stream=True)
	total_size = int(response.headers.get("content-length", 0))
	block_size = 1024
	progress_bar = tqdm(desc=" Downloading... {}.zip".format(VulnBox_NAME), total=total_size, unit="iB", unit_scale=True)

	buffer = BytesIO()
	for data in response.iter_content(block_size):
		buffer.write(data)
		progress_bar.update(len(data))

	progress_bar.close()

	with zipfile.ZipFile(buffer) as zipObject: zipObject.extractall(path=VulnBoxDir)
	print("\n")


def List_All_VulnBox():
	try:
		print("\x1b[32m[*] List of all available VulnBoxes:\x1b[0m")
		res = requests.get("https://api.github.com/repos/truocphan/VulnBox/releases").json()
		for release in res:
			try:
				VulnBox_NAME = release["name"].split(":",1)[0]
				VulnBox_TITLE = release["name"].split(":",1)[1]
				print("- \x1b[1;35m" + VulnBox_NAME + "\x1b[1;0m:" + VulnBox_TITLE + (" ( \x1b[33mDownloaded\x1b[0;0m )" if VulnBox_NAME in os.listdir(os.path.join(os.path.expanduser("~"), "PyPI-VulnBox")) else ""))
			except Exception as e:
				pass
	except Exception as e:
		pass
	print("")


def Start_VulnBox(VulnBox_NAME):
	global VulnBoxDir
	if VulnBox_NAME == "WP-XDEBUG": VulnBoxDir = os.path.join(os.path.expanduser("~"), "Desktop")

	BoxNameDir = os.path.join(VulnBoxDir, VulnBox_NAME)
	BoxComposeFile = os.path.join(VulnBoxDir, VulnBox_NAME, "docker-compose.yaml")

	if os.path.isdir(BoxNameDir): shutil.rmtree(BoxNameDir)

	try:
		download_and_extract_zip(VulnBox_NAME, VulnBoxDir)
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


def Run_VulnBox(VulnBox_NAME):
	global VulnBoxDir
	if VulnBox_NAME == "WP-XDEBUG": VulnBoxDir = os.path.join(os.path.expanduser("~"), "Desktop")

	BoxComposeFile = os.path.join(VulnBoxDir, VulnBox_NAME, "docker-compose.yaml")

	if not os.path.isfile(BoxComposeFile):
		try:
			download_and_extract_zip(VulnBox_NAME, VulnBoxDir)
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


def Delete_VulnBox(VulnBox_NAME):
	global VulnBoxDir
	if VulnBox_NAME == "WP-XDEBUG": VulnBoxDir = os.path.join(os.path.expanduser("~"), "Desktop")

	BoxNameDir = os.path.join(VulnBoxDir, VulnBox_NAME)

	if os.path.isdir(BoxNameDir):
		shutil.rmtree(BoxNameDir)
		print("[+] The VulnBox name \"\x1b[1;32m"+VulnBox_NAME+"\x1b[1;0m\" has been successfully removed.")
	else:
		print("\x1b[1;31m[-] The VulnBox name \""+VulnBox_NAME+"\" does not exist.\x1b[1;0m")


def Update(): os.system("{} -W ignore -m pip install TP-VulnBox --upgrade".format(sys.executable))

def Current_Version():
	p = subprocess.Popen("{} -W ignore -m pip show TP-VulnBox".format(sys.executable), stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	version = re.findall("Version: (\\d{4}\\.\\d{,2}\\.\\d{,2})", output.decode())[0]
	print(" The current version of TP-VulnBox running is \x1b[0;32m{}\x1b[0;0m".format(version))

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

	parser = argparse.ArgumentParser(prog="TP-VulnBox", epilog="\x1b[0;33mVulnBox is a container that is intentionally designed with vulnerabilities to allow security professionals to practice and improve their offensive security skills, such as penetration testing and vulnerability assessment.\x1b[0;0m")
	parser.add_argument("--list-all", action="store_true", help="Lists all available VulnBoxes")
	parser.add_argument("--start", metavar="VulnBox_NAME", type=str, help="Download and run the new VulnBox (e.g. CVE-2024-31211)")
	parser.add_argument("--run", metavar="VulnBox_NAME", type=str, help="Run an existing VulnBox or run a new VulnBox if not already downloaded (e.g. CVE-2024-31211)")
	parser.add_argument("--delete", metavar="VulnBox_NAME", type=str, help="Delete downloaded VulnBox (e.g. CVE-2024-31211)")
	parser.add_argument("--update", action="store_true", help="Update TP-VulnBox to the latest version")
	parser.add_argument("--version", action="store_true", help="Print the current version of TP-VulnBox")
	args = parser.parse_args()

	if args.list_all:
		List_All_VulnBox()
	elif args.start:
		Start_VulnBox(args.start.replace("/", "").replace("\\", "").replace("..", ""))
	elif args.run:
		Run_VulnBox(args.run.replace("/", "").replace("\\", "").replace("..", ""))
	elif args.delete:
		Delete_VulnBox(args.delete.replace("/", "").replace("\\", "").replace("..", ""))
	elif args.update:
		Update()
	elif args.version:
		Current_Version()
	else:
		parser.print_help()

if __name__ == "__main__":
	main()