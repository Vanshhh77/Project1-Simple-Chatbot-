class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I assist you today?"

    def respond_to_question(self, question):
        responses = {
            "How are you?": "I'm doing well, thank you!",
            "What's your name?": "I'm just a simple chatbot.",
            "How does the weather look?": "I don't have access to real-time weather information, sorry!",
            "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
            "What can you do?": "I can answer basic questions and engage in simple conversations.",
        }

        return responses.get(question, "I'm not sure how to answer that.")

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask later."

    def ask_user_questions(self):
        questions = [
            "What is your favorite color?",
            "How was your day?",
            "Have you tried any new hobbies lately?",
        ]

        for question in questions:
            user_response = input(question + " ")
            self.context[question] = user_response
            print("Chatbot: That's interesting! Tell me more.")

    def handle_user_input(self, user_input):
        if "bye" in user_input.lower():
            return self.farewell()

        response = self.respond_to_question(user_input)

        if response == "I'm not sure how to answer that.":
            print("Chatbot: I'm sorry, I didn't understand. Can you please rephrase?")
        else:
            print(f"Chatbot: {response}")

    def chat(self):
        print(self.greet())
        self.ask_user_questions()

        while True:
            user_input = input("User: ")
            if not user_input:
                continue

            if "bye" in user_input.lower():
                print(self.farewell())
                break

            self.handle_user_input(user_input)


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
