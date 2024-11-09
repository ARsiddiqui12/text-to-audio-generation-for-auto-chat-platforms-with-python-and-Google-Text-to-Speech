import os

from  gtts import gTTS

from  datetime import datetime

print("Waiting a user connectivity...")

ConnectedUserID: int = 1 #Make it dynamic

ConnectedUserCountry = "US" #Make it dynamic

DnT = datetime.now()

FileNameDnT = DnT.strftime("%Y-%m-%d_%H-%M-%S")


country = ("US","CN","IT","FR","DE")

Lang = {
"US":"en",
"CN":"zh",
"IT":"it",
"FR":"fr",
"DE":"de"
}

WhatsappMessage = "In my project, this parameter is dynamic. The text is fetched from an API based on the selected language. If the language is English, the text will be in English, and similarly, it will adapt to other languages as needed. Please test this code, and let me know if you find any mistakes. Thank you!"

if len(ConnectedUserCountry) > 2:
    print(f"{ConnectedUserCountry} is not in the records.")

elif ConnectedUserCountry in country:

     language = Lang[ConnectedUserCountry] #Make it dynamic

     speech = gTTS(text=WhatsappMessage, lang=language)

     audio_file = f"{ConnectedUserCountry}_user_{ConnectedUserID}_{FileNameDnT}_{language}.mp3"

     speech.save(audio_file)
else:
    print(f"{ConnectedUserCountry} is not in the records. Please try again.")

