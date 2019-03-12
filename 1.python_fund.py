"""

python3 --version - get version
sudo pip3 install Flask - write in console log to install Flask framework (sudo means "as admin")
pip3 freeze --local - produces list in console log of installed frameworks/packages
pip3 freeze --local > requirements.txt - produces list in the text files of installed frameworks/packages
sudo pip3 install -r requirements.txt - installs the listed packages within the text file
-r stands for recursion. This command says 'install recursively from my requirements.txt file
pip3 uninstall Flast - will unstall Flask or any other package

"""

def print_message(message):
    print(message)
    
print_message("Hello World!")