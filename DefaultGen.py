import sys
import random
import string

letters = string.ascii_letters
typenames = []
MEMBER_NAME_LENGTH = random.randint(5, 30)
CLASS_NAME = ''.join(random.choice(letters) for i in range(MEMBER_NAME_LENGTH))

fwrite = open('default.cpp', 'w')
fwrite.write('// cpp_file\n')
fwrite.write(CLASS_NAME + '::' + CLASS_NAME + '()\n')

typename = ''.join(random.choice(letters) for i in range(MEMBER_NAME_LENGTH))
typenames.append(typename)
value = ('123', '1874', '"random_str"', 'CONST_MACRO')

random_value = random.randint(0,3)
fwrite.write('\t: ' + typename + '(' + value[random_value] + ')\n')
            
FILE_LINES = 1000
for i in range(FILE_LINES - 2):
    MEMBER_NAME_LENGTH = random.randint(5, 30)
    typename = ''.join(random.choice(letters) for i in range(MEMBER_NAME_LENGTH))
    typenames.append(typename)

    random_value = random.randint(0,3)
    fwrite.write('\t, ' + typename + '('+value[random_value]+')\n')
fwrite.write('{\n}\n')
fwrite.close()

fwrite = open('default.hpp', 'w')
fwrite.write('class ' + CLASS_NAME + '\n{\n')
fwrite.write('\t ' + CLASS_NAME + '();\n\n')

for member in typenames:
    MEMBER_TYPE_LENGTH = random.randint(5, 30)
    typename = ''.join(random.choice(letters) for i in range(MEMBER_TYPE_LENGTH))
    fwrite.write('\t ' + typename + ' ' + member + ';\n')
fwrite.write('};\n')
fwrite.close()