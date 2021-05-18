from googletrans import Translator
import googletrans
input = input("Message: ")
t= Translator()
a=t.translate(input,src="vi",dest="en")
print(a.text)
