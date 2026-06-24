import string
def ceaser_chiper(text, shift):
    encrypted_message = ""
    for char in text:
        ascii_value = ord(char)
        updated_ascii_value = ascii_value + shift
        if char is string.ascii_uppercase:
            if updated_ascii_value > 90:
                updated_ascii_value = updated_ascii_value - 90 + 65
        elif char in string.ascii_lowercase:
            if updated_ascii_value > 122:
                updated_ascii_value = updated_ascii_value - 122 + 97
        else:
            updated_ascii_value = updated_ascii_value
        encrypted_message += chr(updated_ascii_value)
    return encrypted_message

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift: "))
    encrypted_text = ceaser_chiper(text, shift)
    print(encrypted_text)

main()