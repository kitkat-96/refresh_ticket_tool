# Glastonbury Sale Refresh Tool

## Running on local machine Mac

Requirements:
* Git must already be installed on your local machine. 
* Python and pip must already be installed on your local machine. 
* Must have Firefox installed.

If you do not have these please follow this [link](https://brew.sh/) to see how to set up brew. You can then run these commands to get Python and Git:
```bash
brew install python
brew install git
```

Steps:
1. Using the Terminal, move into the directory that you wish to clone the git repository into using the cd command. 
2. If you would like to check what files are in your folder, or what folder you are in run the following commands:
```bash
ls
pwd
```
3. In the directory clone the git repository by running the following command:
```bash
git clone https://github.com/klovell96/own_bot.git
```
4. Move into the own_bot folder by using the following command:
```bash
cd own_bot
```
5. Within the own_bot folder, run the following commands: 
```bash
source env/bin/activate
pip install -r requirements.txt
```
6. Now we are ready to run the refresh script. Run the following command:
```bash
python final_firefox.py
```

## Running on local machine Windows

Requirements:
* Git must already be installed on your local machine. 
* Python and pip must already be installed on your local machine. 
* Must have Firefox installed.

If you do not have these you can download [Git](https://git-scm.com/download/win) and [Python](https://www.python.org/downloads/) using the links. 

Steps:
1. Using Powershell, move into the directory that you wish to clone the git repository into using the cd command. 
2. If you would like to check what files are in your folder, or what folder you are in run the following commands:
```bash
ls
pwd
```
3. In the directory clone the git repository by running the following command:
```bash
git clone https://github.com/klovell96/own_bot.git
```
4. Move into the own_bot folder by using the following command:
```bash
cd own_bot
```
5. Within the own_bot folder, run the following commands: 
```bash
pip install -r requirements.txt
```
6. Now we are ready to run the refresh script. Run the correct file for which browser you are using. If you are using a Mac I recommend you run the Firefox version. This is because the Chrome version crashes on Mac.
```bash
python final_firefox.py
```

## Running on Raspberry Pi
**Disclaimer: I do not have a Raspberry Pi and therefore am unable to test this process, or whether the code works on a Rapsberry Pi**

Notes:
* A Raspberry Pi should come preinstalled with Git and Python. 
* This code should run with Chromium, which is an open-source version of Chrome which works on the Raspberry Pi. 

Steps:
1. Open the Raspberry Pi terminal.
2. Install Chromium by running the following command:
```bash
sudo apt-get install chromium-chromedriver
```
3. Check Chromium has been installed properly by running:
```bash
chromium-browser --version
```
4. Check that Chromium has been installed into the _/usr/lib/chromium-browser/_ folder. If it has not, move it into this folder.
5. In the terminal, move into the directory that you wish to clone the git repository into using the cd command.
6. If you would like to check what files are in your folder, or what folder you are in run the following commands:
```bash
ls
pwd
```
7. In the directory clone the git repository by running the following command:
```bash
git clone https://github.com/klovell96/own_bot.git
```
8. Move into the own_bot folder by using the following command:
```bash
cd own_bot
```
9. Within the own_bot folder, run the following commands 
```bash
source env/bin/activate
pip install -r requirements.txt
```
10. Now we are ready to run the refresh script. Run the following command:
```bash
python final_raspsberry_pi.py
```


Links I used to write the above steps. I recommend looking at Ivan's blog if you are having issues:
* [Medium Blog](https://patrikmojzis.medium.com/how-to-run-selenium-using-python-on-raspberry-pi-d3fe058f011)
* [Ivan Derevianko Blog](https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi)
