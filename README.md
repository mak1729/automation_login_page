# automation_login_page
This project is used to automate the login page of websites like facebook,flipkart,etc using selenium written in python.User has no need to type login and password each time he/she opens that website.Just he/she has to run this script.


Installation

	Python

	Window User:- Go to this url and download -https://www.python.org/downloads/windows/

	Linux/Ubuntu:- Python is inbuilt installed.



	pip Installation

	Linux/Ubuntu

	pip :-  sudo apt update              
	        sudo apt install python-pip
	        pip --version


	Windows

	pip :- Navigate to the directory where python is installed C://Python27
	       Set path of C://Python27 in your environmental variables path
	       Download get.py file from this url :- https://bootstrap.pypa.io/get-pip.py
	       Go to that folder where you have downloaded get-pip.py.
	       Run python get-pip.py
	       Go to C://Python27/Scripts and run command pip freeze.
	       Displays the version number of all modules installed in your Python non-standard library.


	Selenium Installation

	Linux/Ubuntu 

	Selenium:- sudo pip install --upgrade pip
	           sudo pip install selenium

	Windows

	Selenium :- Navigate to folder C://Python27/Scripts/
		    Run pip.exe
		    Type the command install selenium


	Chrome Driver Installation

	Linux/Ubuntu

	Chrome Driver :- wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
			 unzip chromedriver_linux64.zip
			 sudo mv chromedriver /usr/bin/chromedriver
			 sudo chown root:root /usr/bin/chromedriver
			 sudo chmod +x /usr/bin/chromedriver

	Windows

	Chrome Driver :- Download the ChromeDriver binary for your platform here -http://chromedriver.chromium.org/downloads
			 Include the ChromeDriver location in your PATH environment variable
   
