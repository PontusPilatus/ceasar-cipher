def caesar_cipher(mode, text, shift):

    if mode == 'decrypt':
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = 26 if char.isupper() else 26
            char_code = ord(char) + shift % shift_amount

            if char.islower() and char_code > ord('z'):
                char_code -= 26
            elif char.isupper() and char_code > ord('Z'):
                char_code -= 26

            result += chr(char_code)
        else:
            result += char

    return result


mode = input("Choose mode (encrypt/decrypt): ").lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift amount: "))

result = caesar_cipher(mode, text, shift)
print("Result:", result)
