
```
   _                _             _                 _       
  /_\   _ __   ___ | |__   _   _ | |   /\ /\  __ _ | |  ___ 
 //_\\ | '_ \ / __|| '_ \ | | | || |  / //_/ / _` || | / _ \
/  _  \| | | |\__ \| | | || |_| || | / __ \ | (_| || ||  __/
\_/ \_/|_| |_||___/|_| |_| \__,_||_| \/  \/  \__,_||_| \___|
```
                                                            



# Python-Translator
A translator made in python, Can also write and read from a file such as txt

### Explaination:
This python file takes an input from a user and writes the input to a text file made by the user. It then translates the text into the desired language and outputs the translated text on the console but **also writes the translated text** into the file made by the user before.

### Prerequisites: 
1) Install translators package from pypi
- https://pypi.org/project/translators/
- To install using cmd, use
```
pip install --upgrade translators
```
- Source:
```
git clone https://github.com/UlionTse/translators.git
cd translators
python setup.py install
```
2) A file needs to be made in user's desired location.
- The file can be of any text like format, eg txt, py etc.

### Editable Code:
1) Code below the '#can edit' can be customized as you wish
2) ```with open(r'path file\filename.txt', mode='w') as myfile:``` 
-   Here put path file as example 'C:\Users\Username\Desktop\fileName.txt'
   Note: the 'r' before the path is needed if you put the file path as above format.
   If you want to remove r, use '/' or '\\' instead of '\' 

