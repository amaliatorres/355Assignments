# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 3 - Front End Technologies
# Amalia Torres

import OutputUtil as ou

# [0] Perform the usual preliminary tasks as outlined in Assignment #1
# [1] Define a function to read in the United States data from file "us-states.csv" into a two-dimensional list..
def read_file(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        states = [line.strip().split(",") for line in lines]
        return states[0], states[1:]

def main():
    title = "US States"
    alignments = ["l", "l", "l", "r"]
    types = ["S", "S", "S", "N"]
    outputFile = "Assignment3.html"
    headers, states = read_file("Assignment3/States.csv")
    for i in range(len(states)):
        name = states[i][0]
        if name == "New York":
            wikiname = "New_York_(state)"
        else:
            wikiname = name
        href = "https://en.wikipedia.org/wiki/" + wikiname.replace(' ', '_')
        a_attributes = 'href="' + href + '" target="_blank"'
        states[i][0] = ou.create_element(ou.TAG_A, name, a_attributes)
    ou.write_html_file(outputFile, title, headers, types, alignments, states,True)

if __name__ == "__main__":
    main()