# Author: Rachel Goodrich
# Group 10
#
# DONE (Eugene Mondkar): Added parameter for text file path
# DONE (Eugene Mondkar): Tested on 10-05-2021 11:00 pm
# DONE (Eugene Mondkar): Resolve Raised UnicodeEncodeError Exception Error on LINE(87) for German character
# DONE (Eugene Mondkar): Resolve Raised TypeError Exception Error on LINE(87) for German character
# TODO (Eugene Mondkar): Return file path of a specific language's text file for Neha's and Kylan's Analysis code

from langdetect import detect
from bs4 import BeautifulSoup
import os

# There are two functions in this file: detect_language and create_text_file. 
# detect_language can be used inside the crawler to ensure that only the webpages in the correct language are stored

def detect_language(fileName):

#This looks at the first paragraph to detect the language
#It returns a 1 in english, 2 if german, 3 if spanish and 0 if other.
#if detect_language returns less than 1 or not the intended language, then do not continue using that link.

    #open up the file
  html = open(fileName, "r")
  soup = BeautifulSoup(html, 'html.parser')

  # The first paragraph may be empty space, so a loop is used to iterate through until a paragraph without empty space is found
  firstParagraph = ""
  myCounter = 0
  while (firstParagraph == "" and myCounter < 10): #checks until paragraph is not empty and lest than 10 paragraphs have been checked.
    if len(soup.findAll("p")) > 0:
      firstParagraph = firstParagraph + soup.find_all("p")[myCounter].text
    firstParagraph = firstParagraph.strip()
    if (firstParagraph == ""):
      print("Paragraph " + str(myCounter) + " is empty")
    else:
      print("Language will detect by using the text: " + firstParagraph)
    myCounter = myCounter + 1
 
  #detect language

  if str(firstParagraph): #if document is not empty and there is something to translate
    myLanguage = str(detect(str(firstParagraph)))
  else:
    myLanguage = 'xx'

  if(myLanguage == 'en'):
    print("Language detected: English")
    return 1
  elif (myLanguage == 'de'):
    print("Language detected: German")
    return 2
  elif (myLanguage == 'es'):
    print("Language detected: Spanish")
    return 3
  else:
    print("Language detected: Other")
    return 0

def create_text_file(fileName, text_files_path, language_num):
#This fully parses the html file and creates/appends the text to a file depending on which language is given.

  #open up the file
  html = open(fileName, "r")

  # parse file to retrieve only text
  soup = BeautifulSoup(html, 'html.parser')
  document = ""
  for paragraph in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
    document = document + paragraph.get_text()
    document = document + " "
  document = " ".join(document.split())
  
  if(language_num == 1):
    htmlFileName = "english.txt"
  elif (language_num == 2):
    htmlFileName = "german.txt"
  elif (language_num == 3):
    htmlFileName = "spanish.txt"
  else:
    htmlFileName = "other.txt"

  fullFileName = text_files_path + htmlFileName

  # write text to a text file
  print("Writing to file...")
  f = open(fullFileName, "a")
  for line in document: #TODO: Resolve UnicodeEncodeError and TypeError
    try:
      f.write(line)
    except:
      print("Pure Gibberish") 

  f.write("\n")
  f.close()
  print("finished!")
	
def detect_language_exhaustive(fileName):
	
#This function detects the language by looking at all of the text inside of the html, instead of just the first paragraph like detect_language

  #open up the file
  html = open(fileName, "r")

  # parse file to retrieve only text
  soup = BeautifulSoup(html, 'html.parser')
  document = ""
  for paragraph in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
    document = document + paragraph.get_text()
    document = document + " "
  document = " ".join(document.split())

  # detect language
  if str(document): #if document is not empty and there is something to translate
    myLanguage = str(detect(str(document)))
  else:
    myLanguage = 'xx'
  
  print(myLanguage)
  if(myLanguage == 'en'):
    print("Language detected: English")
    return 1
  elif (myLanguage == 'de'):
    print("Language detected: German")
    return 2
  elif (myLanguage == 'es'):
    print("Language detected: Spanish")
    return 3
  else:
    print("Language detected: Other")
    return 0

def detect_and_create(text_files_path, repository_path, num_of_files):
# this function creates the directory and calls the other functions so that language detection is done on every file in the repository. It takes in the desired path of the text file directiory, the repository path, and the number of files in the repository.

  directory_exists = os.path.isdir(text_files_path)

  if not directory_exists:
    print("Creating text file directory...")
    os.mkdir(text_files_path)

  print(text_files_path)
  num_of_files = int(num_of_files)

  for current_html_number in range(num_of_files):

    html_file_name = "{:04d}".format(current_html_number) + "_html_file.html"
    print(html_file_name)
    full_path_name = repository_path + html_file_name
    print(full_path_name)
    languageNum = detect_language_exhaustive(full_path_name)
    create_text_file(full_path_name, text_files_path, languageNum)

  print("finished!")
