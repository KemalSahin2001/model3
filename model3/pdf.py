from pdfminer.high_level import extract_text
import time



def extract_pdf():
	text = extract_text("child.pdf")
	return text



