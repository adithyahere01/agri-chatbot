from chatterbot import ChatBot

bot = ChatBot("units", logic_adapters=["chatterbot.logic.UnitConversion"])

print("-----Unit-----")
while True:
    user_text = input("Ask a unit convo: ")
    print("Chatbot: " + str(bot.get_response(user_text)))
