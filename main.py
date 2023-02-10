import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Morse_code"

response = requests.get(URL)
morse_code = response.text

soup = BeautifulSoup(morse_code, "html.parser")

td_tags = soup.find_all("td")

morse_encode = {}
morse_decode = {}

for td in td_tags:
    if td.text.strip() == "Letters":
        morse_encode[f"{td.find_next_sibling(name='td').text[0]}"] = td.find_next_sibling(name='td').find_next_sibling(
            name='td').find('span').text.strip().replace('▄▄▄', '-').replace('▄', '.').replace(' ', '')
        morse_decode[
            f"{td.find_next_sibling(name='td').find_next_sibling(name='td').find('span').text.strip().replace('▄▄▄', '-').replace('▄', '.').replace(' ', '')}"] = \
            td.find_next_sibling(name='td').text[0]

    if td.text.strip() == "Numbers":
        morse_encode[f"{td.find_next_sibling(name='td').text[0]}"] = td.find_next_sibling(name='td').find_next_sibling(
            name='td').find('span').text.strip().replace('▄▄▄', '-').replace('▄', '.').replace(' ', '')
        morse_decode[
            f"{td.find_next_sibling(name='td').find_next_sibling(name='td').find('span').text.strip().replace('▄▄▄', '-').replace('▄', '.').replace(' ', '')}"] = \
            td.find_next_sibling(name='td').text[0]


def morse(text_morse, morse_direction):
    morse_result = str("")
    if morse_direction == "encode":
        letters = text_morse.upper()
        for string in letters:
            if string.isspace():
                morse_result += "/ "
            else:
                morse_result += f"{morse_encode[string]} "
    else:
        list_morse = text_morse.strip().split(' ')
        for item in list_morse:
            if item == "/":
                morse_result += " "
            else:
                morse_result += morse_decode[item]

    print(f"Here's the {morse_direction}d result: {morse_result}")


print("Welcome to the Morse Code Generator!")
again = True
while again:
    direction = input("Type 'encode' to generate morse code, type 'decode' to decrypt morse code:\n")
    text = input("Type your message:\n")
    morse(text_morse=text, morse_direction=direction)
    choice = input("Type 'yes' if you want to try again. Otherwise type 'no'\n").lower()
    if choice == "no":
        again = False
        print("Goodbye. Thank you for testing this project.")