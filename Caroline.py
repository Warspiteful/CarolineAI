from collections import Counter
import spacy, re

w2v = spacy.load('en_core_web_sm')

class Caroline():

    exit_commands = ("quit", "goodbye", "exit", "no")

    def exit(self, user_message):
        for word in user_message:
            if word in exit_commands:
                print("Goodbye")
                return True
        return False

    def match_intent(self):
        pass

    def find_entities(self,user_input):
        pass

    def chat(self):
        reply = input("Insert Placeholder here")
        while not self.exit(reply):
            reply = self.parse_response(reply)

    def parse_response(self, user_message):
        pass
