import sys
import random
import string

letters = string.ascii_uppercase
            
PRAGMA_FILES_COUNT = 1000
for i in range(PRAGMA_FILES_COUNT):
    tokens = random.randint(1, 4)
    macro = ''
    for j in range(tokens):
        TYPE_LENGTH = random.randint(7, 12)
        token_name = ''.join(random.choice(letters) for i in range(TYPE_LENGTH))
        macro = macro + token_name + '_'
    macro = macro + 'HPP'
    fwrite = open('pragma_' + str(i) + '.hpp', 'w')
    fwrite.write('#ifndef ' + macro + '\n')
    fwrite.write('#define ' + macro + '\n\n')
    fwrite.write('#endif // ' + macro)
    fwrite.close()