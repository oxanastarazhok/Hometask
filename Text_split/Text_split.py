message = ("How are you? Eh, ok. Low or Lower? Ohh.")

def find_secret_message(message):
    secret_message = ""
    for letter in message:
        if letter.isupper():
            secret_message += letter
    return secret_message
print find_secret_message("How are you? Eh, ok. Low or Lower? Ohh.")