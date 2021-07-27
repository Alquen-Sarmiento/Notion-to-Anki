from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="3e3b1b28588d798b7a4dc957c82b26cd2aca95b06e54beb51871e3117a572b237cbbf3e0396cb9caa674c6542f154d0d2e7231fbb7198ab963935c8eba6abd83464cb3fee62edfc48f3b633c2afb")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("https://www.notion.so/alquen/Notion-API-Test-a0c6081945e54291984405430af9a098")

# Temporary storage
flashcards = []

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

for child in page.children:
    if child.type == 'toggle':
        flashcards.append(Flashcard(child.title, child.children[0].title))