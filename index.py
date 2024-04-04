from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests


app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False, logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "I'm still processing your question with my exisitng models and trying to learn from it!",
        "maximum_similarity_threshold":  0.9
    },
    {
        "import_path": "chatterbot.logic.MathematicalEvaluation"
    }
])


list_to_train = [
    "Hi",
  "Hello there! How can I assist you with agriculture today?",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "Hi",
    "Welcome, friend 🤗",
    "Are you a plant?",
    "No, I'm the pot below the plant!",
     "What crops should I grow?",
  "The best crops to grow depend on your location, climate, and soil type. Can you provide more details?",
    "How to control pests in my crops?",
  "There are several methods for pest control, including natural predators, organic pesticides, and crop rotation. Which crop are you concerned about?",
    "What's the weather forecast for tomorrow?",
  "I can't provide real-time weather forecasts. You may want to check a reliable weather website or app for the most accurate information.",
    "How much water should I give to my crops?",
  "Different crops have different water requirements. Generally, it's essential to maintain soil moisture levels consistent with the crop's needs. Overwatering or underwatering can both be harmful.",
     "What crops should I grow in a temperate climate?",
   "In a temperate climate, crops like wheat, barley, oats, potatoes, carrots, and apples tend to thrive. However, specific recommendations can vary based on your location and soil conditions.",
    "How do I improve soil fertility?",
    "Soil fertility can be enhanced through practices like crop rotation, adding organic matter (compost or manure), using cover crops, and balancing soil pH with lime or sulfur.",
    "How do I prevent diseases in my tomato plants?",
    "To prevent diseases in tomato plants, practice crop rotation, provide adequate spacing between plants, avoid overhead watering, and apply fungicides if necessary. Additionally, choose disease-resistant tomato varieties.",
    "Can you suggest some organic pest control methods?",
    "Certainly! Organic pest control methods include introducing beneficial insects, using neem oil or insecticidal soap, planting companion plants that repel pests, and maintaining healthy soil and plants.",
    "How much sunlight do citrus trees need?",
    "Citrus trees typically require full sun exposure, which means at least 6-8 hours of direct sunlight per day for optimal growth and fruit production.",
    "When is the best time to harvest strawberries?",
  "Strawberries are usually ready for harvest when they turn fully red, usually in late spring or early summer depending on the variety and local climate. Harvest them in the morning when temperatures are cooler.",
    "What's the difference between organic and conventional farming?",
  "Organic farming avoids synthetic pesticides and fertilizers, focuses on soil health and biodiversity, and emphasizes sustainable practices. Conventional farming relies more on synthetic inputs for pest control and soil fertility.",
    "How can I conserve water in my garden?",
  "You can conserve water in your garden by using mulch to retain moisture, watering plants deeply but less frequently, installing drip irrigation systems, collecting rainwater in barrels, and choosing drought-tolerant plant varieties.",
    "Thank you for your help!",
    "You're welcome! If you have any more questions in the future, feel free to ask. Happy gardening!",
    "What's the weather like tomorrow in New York City?",
    "The weather forecast for tomorrow in New York City predicts partly cloudy skies with a high of 72°F and a low of 58°F. There's a slight chance of rain in the afternoon.",
    "How do meteorologists predict the weather?",
  "Meteorologists use various tools and techniques, including weather satellites, radar systems, weather balloons, computer models, and historical data analysis to forecast the weather. It's a complex process that involves analyzing atmospheric conditions and patterns.",
    "What's the difference between weather and climate?",
  "Weather refers to short-term atmospheric conditions in a specific location, such as temperature, humidity, precipitation, and wind. Climate, on the other hand, refers to long-term patterns and averages of weather conditions in a particular region over time, typically spanning decades or centuries.",
    "How accurate are weather forecasts?",
  "Weather forecasts have become increasingly accurate over the years, especially for short-term predictions (1-3 days). However, their accuracy decreases for longer-term forecasts and can vary depending on factors like location, weather patterns, and the complexity of the forecasted conditions.",
    "How can I prepare for severe weather events like hurricanes?",
  "To prepare for severe weather events like hurricanes, you should have an emergency plan in place, stock up on essentials like food, water, batteries, and medications, secure outdoor items, reinforce windows and doors, and stay informed by monitoring weather updates from reliable sources.",
    "What's the difference between a tornado watch and a tornado warning?",
  "A tornado watch means that weather conditions are conducive to the formation of tornadoes in the designated area, while a tornado warning indicates that a tornado has been spotted or indicated by radar, and immediate action should be taken to seek shelter.",
    "How does humidity affect how we perceive temperature?",
  "High humidity levels can make temperatures feel hotter than they actually are because the body's ability to cool itself through sweat evaporation is hindered. Conversely, low humidity levels can make temperatures feel cooler because sweat evaporates more efficiently",
    "Can weather patterns be influenced by climate change?",
  "Yes, climate change can influence weather patterns by altering atmospheric circulation patterns, increasing the frequency and intensity of extreme weather events like heatwaves, hurricanes, and heavy rainfall, and shifting precipitation patterns.",
  "Thank you for the information!"
]

cities = ['Ariyalur',
			'Chennai',
			'Coimbatore',
			'Cuddalore',
			'Dharmapuri',
			'Dindigul',
			'Erode',
			'Kanchipuram',
			'Kanyakumari',
			'Karur',
			'Madurai',
			'Nagapattinam',
			'Nilgiris',
			'Namakkal',
			'Perambalur',
			'Pudukkottai',
			'Ramanathapuram',
			'Salem',
			'Sivaganga',
			'Tirupur',
			'Tiruchirappalli',
			'Theni',
			'Tirunelveli',
			'Thanjavur',
			'Thoothukudi',
			'Tiruvallur',
			'Tiruvarur',
			'Tiruvannamalai',
			'Vellore',
			'Viluppuram',
			'Virudhunagar',]
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")
# trainer.train("chatterbot.corpus.spanish")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get("userMessage")

    if userText in cities:
        rawData = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+userText +"&appid=b84958809e3431d4aef78bab0a1aebe1")
        result = rawData.json()
        print(result)
        return result
    return str(bot.get_response(userText))
    # return result


if __name__ == "__main__":
    app.run(debug=True)

