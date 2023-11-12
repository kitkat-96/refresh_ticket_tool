# Glastonbury Sale Refresh Tool

## Running on local machine

Requirements:
* Git must already be installed on your local machine. 
* Python and pip must already be installed on your local machine. 
* Must have either Firefox or Chrome installed. If you are using a Mac, I recommend you install Firefox.

Steps:

1. Using the terminal, move into the directory that you wish to clone the repository into using the cd command. 
2. In the directory clone the git repository by running the following command:
```bash
git clone https://github.com/klovell96/own_bot.git
```
3. Move into the own_bot folder by using the following command:
```bash
cd own_bot
```
4. Within the own bot folder, run the following commands 
```bash
source env/bin/activate
pip install -r requirements.txt
```
5. Now we are ready to run the refresh script. Run the correct file for which browser you are using. If you are using a Mac I recommend you run the Firefox version. This is because the Chrome version crashes on Mac.
```bash
python final_chrome.py
python final_firefox.py
```

## Running on Raspberry Pi


```bash
sudo apt-get install chromium-chromedriver
```

