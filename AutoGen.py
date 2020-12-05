import sys
import random
import string

if len(sys.argv) != 5:
    print('pass 4 args')
    print('1 - for')
    print('2 - if')
    print('3 - ptr')
    print('4 - iterator')
    sys.exit(0)

FOR_CHANCE = ('for', int(sys.argv[1]))
IF_CHANCE = ('if', int(sys.argv[2]))
SMART_PTR_CHANCE = ('ptr', int(sys.argv[3]))
ITERATOR_CHANCE = ('iterator', int(sys.argv[4]))

if FOR_CHANCE[1] + IF_CHANCE[1] + SMART_PTR_CHANCE[1] + ITERATOR_CHANCE[1] != 100:
    print('chances rate must sum up to 100')
    sys.exit(0)

letters = string.ascii_letters
def append_line(f, instr):
    TYPE_LENGTH = random.randint(15, 15)
    typename = ''.join(random.choice(letters) for i in range(TYPE_LENGTH))
    if instr == 'for':
        fwrite.write('for (' + typename + ' i = x.get(); i < x + N; ++i) { i.member = 34 }\n')
        pass
    elif instr == 'if':
        fwrite.write('if (' + typename + ' i = y.next) { i.member = 34 }\n')
        pass
    elif instr == 'ptr':
        fwrite.write('std::shared_ptr<' + typename + '> ptr = std::make_shared<' + typename + '>();\n')
        pass
    elif instr == 'iterator':
        fwrite.write('std::map<' + typename + '>::iterator it = myMap.begin();\n')
        pass

chances = sorted([FOR_CHANCE, IF_CHANCE, SMART_PTR_CHANCE, ITERATOR_CHANCE], key=lambda x: x[1])

fwrite = open('auto.cpp', 'w')

A = chances[0][1]
B = chances[0][1] + chances[1][1]
C = chances[0][1] + chances[1][1] + chances[2][1]
D = chances[0][1] + chances[1][1] + chances[2][1] + chances[3][1]

FILE_LINES = 1000
for i in range(FILE_LINES):
    random_int = random.randint(1, 100)
    if 1 <= random_int <= A:
        append_line(fwrite, chances[0][0])
    elif A <= random_int <= B:
        append_line(fwrite, chances[1][0])
    elif B <= random_int <= C:
        append_line(fwrite, chances[2][0])
    elif C < random_int <= 100:
        append_line(fwrite, chances[3][0])

fwrite.close()