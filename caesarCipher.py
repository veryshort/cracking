#
#

import pyperclip

#
message = 'This is my secret message.'
# message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# The encryption/decryption key:
key = 13

#
mode = 'encrypt'
# mode = 'decrypt'

#
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#
translated = ''

for symbol in message:
    #
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #
        translated = translated + symbol

#
print(translated)
pyperclip.copy(translated)
