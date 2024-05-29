import PyPDF2
import pyttsx3

def audiobook():
    book = open('oop.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages) 
    speaker = pyttsx3.init()
    for num in range(7, pages):
        page = pdfReader.pages[7]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()
