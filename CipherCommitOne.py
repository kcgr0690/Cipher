import time

keep_going = True

while keep_going == True:
    
    ans = input("Would you like to encode (enter 'E') or decode (enter 'D')\n\n").lower()

    def encode():

        cipher_dict = {
        'a': '∆', 'b': '⊗', 'c': 'ʘ', 'd': '≈', 'e': 'ξ', 'f': '☼',
        'g': '♣', 'h': '☾', 'i': '∑', 'j': '≠', 'k': '♠', 'l': '♦',
        'm': '♫', 'n': '⊕', 'o': '◉', 'p': '∞', 'q': '⌘', 'r': '☯',
        's': '★', 't': '✿', 'u': '✓', 'v': '⚑', 'w': '☂', 'x': '✦',
        'y': '☠', 'z': '✉', '!': '!', '@': '@', '#': '#', '$': '$', 
        '%': '%', '^': '^', '&': '&', '*': '*', '(': '(', ')': ')', ' ': '  ',
          ',': ',', '.': '.', '?': '?', ';': ';', '/': '/', '<': '<', '>': '>', 
    }
        secretMessage = input("\nWhat's your secret message?\n\n").lower()

        time.sleep(1)

        print("\nYour encoded message is:\n")

        encoded = ""

        for i in secretMessage:
            encoded += cipher_dict[i]
        
        time.sleep(1)

        print(encoded)

    def decode():
        decode_dict = {
        '∆':'a','⊗':'b','ʘ':'c','≈':'d','ξ':'e','☼':'f','♣':'g','☾':'h',
        '∑':'i','≠':'j','♠':'k','♦':'l','♫':'m','⊕':'n','◉':'o','∞':'p',
        '⌘':'q','☯':'r','★':'s','✿':'t','✓':'u','⚑':'v','☂':'w','✦':'x',
        '☠':'y','✉':'z','!':'!','@':'@','#':'#','$':'$','%':'%','^':'^',
        '&':'&','*':'*','(':'(',')':')',' ':' ', ',': ',', '.': '.', '?': '?',
          ';': ';', '/': '/', '<': '<', '>': '>', 
    }
        encodedMessage = input("What's the encoded message?\n\n")
        
        time.sleep(1)

        print("\nThe decoded message is:\n")

        time.sleep(1)

        for i in encodedMessage:
            print(decode_dict[i], end = "")
        print("\n")



    if ans == "e":
        encode()
    else:
        decode()

    time.sleep(1)

    continueLoop = input("\n\nWould you like to continue (enter Y) or quit (enter Q)? \n").lower()

    if continueLoop == "q":
        keep_going = False
