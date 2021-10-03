from langdetect import detect
from bs4 import BeautifulSoup

# There are two functions in this file: detect_language and create_text_file. 
# detect_language can be used inside the crawler to ensure that only the webpages in the correct language are stored

def detect_language(fileName, repository_path):

#This looks at the first paragraph to detect the language
#It returns a 1 in english, 2 if german, 3 if spanish and 0 if other.
#if detect_language returns less than 1 or not the intended language, then do not continue using that link.

    #open up the file
  fullFileName = repository_path + fileName
  html = open(fullFileName, "r")
  soup = BeautifulSoup(html, 'html.parser')

  # The first paragraph may be empty space, so a loop is used to iterate through until a paragraph without empty space is found
  firstParagraph = ""
  myCounter = 0
  while (firstParagraph == ""):
    firstParagraph = soup.find_all("p")[myCounter].text
    firstParagraph = firstParagraph.strip()
    if (firstParagraph == ""):
      print("Paragraph " + str(myCounter) + " is empty")
    else:
      print("Language will detect by using the text: " + firstParagraph)
    myCounter = myCounter + 1
 
  #detect language
  myLanguage = str(detect(str(firstParagraph)))
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

def create_text_file(fileName, repository_path, language_num):
#This fully parses the html file and creates/appends the text to a file depending on which language is given.

  #open up the file
  fullFileName = repository_path + fileName
  html = open(fullFileName, "r")
  soup = BeautifulSoup(html, 'html.parser')
  document = ""

    #find all text
  for paragraph in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
    document = document + paragraph.get_text()

  if(language_num == 1):
    htmlFileName = "english.txt"
  elif (language_num == 2):
    htmlFileName = "german.txt"
  elif (language_num == 3):
    htmlFileName = "spanish.txt"
  else:
    htmlFileName = "other.txt"

  fullFileName = repository_path + htmlFileName

  # write text to a text file
  print("Writing to file...")
  f = open(fullFileName, "a")
  for line in document:
	  f.write(line)
  f.close()
  print("finished!")
	
def detect_language_exhaustive(fileName, repository_path):
	
#This function detects the language by looking at all of the text inside of the html, instead of just the first paragraph like detect_language

  #open up the file
  fullFileName = repository_path + fileName
  html = open(fullFileName, "r")
  soup = BeautifulSoup(html, 'html.parser')
  document = ""

  #find all text
  for paragraph in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
    document = document + paragraph.get_text()

  #remove all extra white space and all new line characters
  document = document = " ".join(document.split())

  # detect language
  myLanguage = str(detect(str(document)))
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
