import datetime
import string
from random import randint, choice

HISTORY_LENGTH = 30

fwrite = open('comments.cpp', 'w')
fwrite.write('/* file history \n')
dates = []

letters = string.ascii_letters
for i in range(HISTORY_LENGTH):
    date = datetime.date(randint(2000,2010), randint(1,12),randint(1,28)).strftime("%Y-%m-%d")
    dates.append(date)

for date in sorted(dates):
    AUTHOR_NICK_LENGTH = randint(5, 30)
    author = ''.join(choice(letters) for i in range(AUTHOR_NICK_LENGTH))
    fwrite.write('  ' + date + '  ' + author + ' some comment here\n')
fwrite.write('*/\n')

instructions = ('try', 'if', 'for', 'while', 'switch')

def generate_instruction(instr):
    if instr == 'try':
        fwrite.write('try\n{\n    // try code here\n} // try\ncatch (std::exception& err)\n{\n    // catch code here\n} // catch (std::exception& err)\n')
    elif instr == 'if':
        fwrite.write('if (true)\n{\n    // if code here\n} // if (true)\nelse\n{\n    // else code here\n} // else\n')
    elif instr == 'for':
        fwrite.write('for (int i = 0; i < N; ++i)\n{\n    // for code here\n} // for (int i = 0; i < N; ++i)\n')
    elif instr == 'while':
        fwrite.write('while (i < N)\n{\n    // while code here\n    ++i;\n} // while (i < N)\n')
    elif instr == 'switch':
        fwrite.write('switch (variable)\n{\n    case 1:\n        k++;\n    case 2:\n        j++;\n} // switch (variable)\n')

INSTRUCTIONS_COUNT = 3000

for i in range(INSTRUCTIONS_COUNT):
    i = randint(0, len(instructions)-1)
    generate_instruction(instructions[i])

fwrite.close()

