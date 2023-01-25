# Before using open `cmd` and paste `cd target/directory` `then dir /b>list.txt`

from googletrans import Translator
import os


translator = Translator()
directoryPath = '/roadmaps/vue/content/102-ecosystem/106-api-calls/'
destFile = f'./dir{directoryPath}list.txt'
rootFile = open(destFile, 'r')

def translate_requestUKR(text):
   return translator.translate(text, dest='uk').text

def translate_requestRUS(text):
   return translator.translate(text, dest='ru').text

  
def main():
    for currentLine in rootFile:
        if not currentLine:
            break
        if 'list.txt' not in currentLine:
            if '.md' in str(currentLine) and '.' in str(currentLine):
                try: 
                    with open(f'./dir{directoryPath}{currentLine.strip()}', encoding='utf8') as extractText:
                        content = extractText.read()

                    with open(f'./ukr{directoryPath}{currentLine.strip()}', "w", encoding='utf8') as saveTranslate:
                        saveTranslate.write(translate_requestUKR(content))
                        # saveTranslate.write(content)
                        print(f"[+] Translated File Path: ./ukr{directoryPath}{currentLine.strip()}")       
                    with open(f'./rus{directoryPath}{currentLine.strip()}', "w", encoding='utf8') as saveTranslate:
                        saveTranslate.write(translate_requestRUS(content))
                        # saveTranslate.write(content)
                        print(f"[+] Translated File Path: ./rus{directoryPath}{currentLine.strip()}")   
                except FileNotFoundError:
                    continue
            elif '.' not in str(currentLine):
                print(f"[-] Can't translate. Seems like directory: {currentLine.strip()}")
    rootFile.close()
    os.unlink(destFile)
    print('\nSuccess!')

if __name__ == '__main__':
    main()