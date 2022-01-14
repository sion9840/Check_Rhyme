from ko_pron import romanise #한국어 to ipa 라이브러리 #romanise(val, "ipa")
import eng_to_ipa as ipa #영어 to ipa 라이브러리 #ipa.convert(val)

def inputLyrics():
    string_lyrics = ""

    for i in range(1000):
        string_line_input = input()
        if string_line_input == "---":
            break
        else:
            if string_line_input == "":
                string_lyrics = string_lyrics + "\n"

            string_lyrics = string_lyrics + string_line_input + "\n"

    string_lyrics = string_lyrics[:-1]

    return string_lyrics, string_lyrics.replace("\n", " ").split(" ")

def transStringToIpa(string):
    for char in string:
        pass


string_lyrics, list_lyrics = inputLyrics()
ipa_lyrics = ""

print(string_lyrics)