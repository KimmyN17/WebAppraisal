### Setting Up the Django Project
1. Install [Python version 3.7.4](https://www.python.org/downloads/release/python-374/) for your OS
   * After installing, validate that it was successful by running the command `python3 --version`
   * Also ensure that pip was installed alongside python by running the command `pip --version`

   *In Windows: If you type 'py' it will show you python version number and enter the python shell. type 'exit()' to leave.           
   *In Windows: Type 'py -m pip --version' in CMD Prompt to see pip verion number

2. Create a clone of our GitHub repository, which can be found [here](https://github.com/Bshuryan/WebAppraisal).
    1. Run the command `git clone https://github.com/Bshuryan/WebAppraisal` `<insert desination directory>`
       * Note: You must specify a project name, so I would recommend the desination directory be `some/directories/WebAppraisal`, which will create a new folder titled `WebAppraisal` under `some/directories/`
    
     2. An alternative method: you can download GitHub Desktop, select file in the top left --> clone directory.  From here you will see the GitHub projects attached to your account.  Clone the WebAppraisal Project.

3. Set up your virtual environment. (MAC)
   1. Run the command `virtualenv -p python3 venv`, which will create a new directory, `venv`
   2. Activate your virtual environment by running `source venv/bin/activate`
   3. Install Django using pip by running the command `pip install django==3.1.5`

4. Set up Virtual env in Windows.

   0. Make sure Django is installed by running the following in CMD prompt "py -m pip install Django"
   1. login to pycharm and Open cloned project from GitHub
   2. On the bottom of the pycharm window select Terminal
   3. Find where your python install is located, you will need to run the command in terminal from this directory. **You can do this by running this command in CMD Prompt "py -c "import os, sys; print(os.path.dirname(sys.executable))"
   4. change directorys in terminal to the file path given in the above cmd
   5. once in the correct directory run 'py -m venv C:\"YourFilePathOfGitHubProject"\venv     *It is important to remember the folder name after your GitHub Project File Path in order to create a folder and avoid installing in the root of your project
     *Running this correctly should get you a new folder in your pycharm client in the WebAppraisal project called "venv"
   6. activate your virtual enviorment with venv\scripts\activate in CMD prompt
   7. in pycharm, double click the shift key and type in "base" in the search box. Open up the base webApprasial.settings file, and press cntrl F to search for the "SECRET_KEY" variable. Replace the value to SECRET_KEY = 'secretkeyvalue' (secret key can be found in the discord)
    
### Running Locally
(MAC)

1. While in your virtual environment and at the top level of the project directory, run the command `python manage.py runserver`
2. Visit http://127.0.0.1:8000/, which will direct you to the landing page for our webapp.

(WINDOWS)

1. while in CMD prompt and have you venv active type 'py manage.py runserver'
2. Visit http://127.0.0.1:8000/, which will direct you to the landing page for our webapp.


### Running in Production Environment
* We are quite there yet


### FAQ
Q: Why am I getting an error `"Set the SECRET_KEY environment variable"`?

A: You may be running the project locally for the first time. Follow these steps to resolve the issue:
1. Request the secret key from a project member.
2. If the request is granted, add the following line to the bottom of `venv/bin/activate` to add the environment variable
    `export SECRET_KEY="Insert Secret Key here"`
3. Deactivate your virtual environment by running `deactivate` while within your virtual environment
4. Re-activate your environment to apply your changes by running `source venv/bin/activate`
5. Retry running `python manage.py runserver`

Q: Why am I receiving an ImportError?

A: You may not have the package requirements. Open up the requirements.txt inside Pycharm. If a message says the requirements are not satisfied, click the "Install Requirements" option.
