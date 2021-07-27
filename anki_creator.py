import genanki
import random

def id_generator():
  return random.randrange(1 << 30, 1 << 31)


main_deck = genanki.Deck(
  id_generator(),
  'Test Questions')


main_model = genanki.Model(
  id_generator(),
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ],
  css="""
  .card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
  }
  """)


def add_card_to_deck(question, answer):
  main_deck.add_note(genanki.Note(
    model=main_model,
    fields=[question, answer]
  ))

def output_to_file():
  genanki.Package(main_deck).write_to_file('output.apkg')