from chatterbot import ChatBot

bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("-----MATH-----")
while True:
    user_text = input("Type math equations: ")
    print("Chatbot: " + str(bot.get_response(user_text)))
