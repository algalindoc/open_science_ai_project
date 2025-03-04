import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import process_papers as process
import extract_data as extract

def menu():

    process.process_papers()
    extract.extract_data()
    extract.plot_figures()
    extract.save_links()
    extract.generate_wordcloud()


if __name__ == "__main__":
    menu()
