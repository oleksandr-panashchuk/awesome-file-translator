# 📂 Awesome File translator

This Python script is used to translate all the .md files in a given directory and its subdirectories from the default language to Ukrainian and Russian.

## 📜 Before using this script

Open the command prompt and install requirements by using the command `pip install -r requirements.txt`

Then open the command prompt in your IDE/IDLE and navigate to the target directory by using the command
`cd target/directory` and then use the command `dir /b>list.txt` to create a list of all files and subdirectories in that directory.

The script uses the **[googletrans](https://pypi.org/project/googletrans/)** library to translate the text. The "Translator" class is imported from the library and used to create an instance of the translator.

The script then defines two functions `translate_requestUKR` and `translate_requestRUS` that take in a text as an argument and return the translated text in Ukrainian and Russian respectively.

The main function of the script reads the list of files and subdirectories from the `list.txt` file, checks if the current line is a file or a directory and if it's a .md file, it opens the file, reads its content, and uses the above defined functions to translate the content to Ukrainian and Russian. The translated content is then saved in new files with the same name but with "ukr" and "rus" added to the file name.

The script also prints the path of the translated files for reference.

Finally, the script closes the `list.txt` file, deletes it and prints `Success!` on the screen when all the translations are done.

It is important to note that this script will only translate the `.md` (*YOU CAN CHANGE IT, JUST REPLACE*) files in the directory, any other files or directories will be ignored.