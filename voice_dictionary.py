import pyttsx3
import speech_recognition as sr #pyttsx3, speech_recognition, and pyaudio are modules required for python to collect speech data, compile it into a string, and play back the response
import pyaudio
from PyDictionary import PyDictionary #module used for the dictionary
dictionary=PyDictionary()
from sys import path
path.append('SET PATH TO FOLDER WITH THE MODULES HERE')

def speaknow(): #use of pyttsx3 module downloaded from PyPI using PIP
	engine = pyttsx3.init() # object creation

	rate = engine.getProperty('rate')   # getting details of current speaking rate
	engine.setProperty('rate', 150)     # setting up new voice rate

	volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
	engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

	voices = engine.getProperty('voices')       #getting details of current voice
	#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
	engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

	engine.runAndWait()
	engine.stop()

	engine.save_to_file('Hello World', 'test.mp3')
	engine.runAndWait()

def starting_prompt(): #function speaks out the starting prompt to the user using pyttsx3
	pyttsx3.speak("Hello user. Say an option that you would like me to find or say goodbye to exit") #starting prompt
	start = 0 
	operation = "Definition.Synonym.Antonym.Translate to spanish." #dictionary options for the user to choose from 
	split = 0
    
	for x in operation: #puts all the characters in between two "." on the same line and then starts a new one
		if x == '.': 
			print(operation[start:split])
			start = split + 1  
		split = split + 1 
	print(operation[start:split]) 
	

def takeoperation(): #function processes which option the user chose (spoke out loud) returns it as a string

	r = sr.Recognizer() #uses speech_recognition module downloaded from PyPI using PIP

	with sr.Microphone() as source:
		r.pause_threshold = 2.0
		audio = r.listen(source)
		
		try:
			query = r.recognize_google(audio, language='en-in')
			
		except Exception as e:
			print(e)
			pyttsx3.speak("Say that again")
			return "None"
		
		return query
	
def takeword(): #function processes the spoken word the user would like to input into the dictionary and returns it as a string
	pyttsx3.speak("say your word")
	r = sr.Recognizer()

	with sr.Microphone() as source:
		r.pause_threshold = 2.0
		audio = r.listen(source)
		
		try:
			word = r.recognize_google(audio, language='en-in')
			
		except Exception as e:
			print(e)
			pyttsx3.speak("Say that again")
			return "None"
		
		return word
	

def calculations(): #function includes a series of if statements to determine which option the user chose and run that option in PyDictionary with the word they input
	starting_prompt()
	while(True):
		query = takeoperation().lower()
		if "goodbye" in query:
			print("Goodbye user")
			pyttsx3.speak("Have a good day user")
			exit()
		word = takeword().lower()
		if "definition" in query:
			print(str(word))
			print(dictionary.meaning(str(word))) #prints dictionary result on console
			pyttsx3.speak(dictionary.meaning(str(word))) #speaks dictionary result to user
			pyttsx3.speak("Have a good day user")
			exit() 
			continue
		elif "synonym" in query:
			print(str(word))
			print(dictionary.synonym(str(word)))
			pyttsx3.speak(dictionary.synonym(str(word)))
			pyttsx3.speak("Have a good day user")
			exit()
			continue
		elif "antonym" in query:
			print(str(word))
			print(dictionary.antonym(str(word)))
			pyttsx3.speak(dictionary.antonym(str(word)))
			pyttsx3.speak("Have a good day user")
			exit()
			continue
		elif "translate to spanish" in query:
			print(str(word))
			print(dictionary.translate(str(word),'es'))
			pyttsx3.speak(dictionary.translate(str(word),'es'))
			pyttsx3.speak("Have a good day user")
			exit()
			continue
		







if __name__ == "__main__": #invokes the calculations function
	calculations()
	
