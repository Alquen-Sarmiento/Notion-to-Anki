import anki_creator
import notion_fetcher

for flash in notion_fetcher.flashcards:
    anki_creator.add_card_to_deck(flash.question, flash.answer)

anki_creator.output_to_file()