import pyttsx3
import PyPDF2
book = open('ai.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speak = pyttsx3.init()
page = pdfReader.getPage(2)
text = page.extractText()
speak.say(text)
speak.runAndWait()