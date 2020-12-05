import datetime
import string
from random import randint, choice

letters_low = string.ascii_lowercase
letters_up = string.ascii_uppercase

tokens = randint(1, 4)
classname = ''
for k in range(tokens):
    TOKEN_LENGTH = randint(2, 5)
    token_name = ''.join(choice(letters_low) for i in range(TOKEN_LENGTH))
    classname = classname + token_name if k == tokens-1 else classname + token_name + '_'


METHODS_COUNT = 500
MEMBERS_COUNT = 2000
types = ('std::vector<int>', 'bool', 'int', 'Type*', 'Typeref&')
hungarian = ('v', 'b', 'i', 'p' ,'r')
# random_lines = ('v', 'b', 'i', 'p' ,'r')

members = []
methods = []
public_methods_params = {}
private_methods_params = {}
public_members = {}
private_members = {}

fwrite = open('convention.hpp', 'w')
fwrite.write('class ' + classname + '\n{\n')

def generate_ctor_dtor(classname):
    fwrite.write('    ' + classname + '();\n')
    fwrite.write('    ~' + classname + '();\n\n')
    
def generate_members(section):
    for i in range(MEMBERS_COUNT):
        r = randint(0, len(types)-1)
        typename = types[r]
        param_name = hungarian[r] + choice(letters_up)
        tokens = 1 # randint(2, 4) # TODO
        for k in range(tokens):
            TOKEN_LENGTH = randint(2, 5)
            token_name = ''.join(choice(letters_low) for i in range(TOKEN_LENGTH))
            param_name = param_name + token_name if k == tokens-1 else param_name + token_name + '_'

        param_name = param_name + '_MEMBER'

        fwrite.write('    ' + typename + ' ' + param_name + ';\n')
            
        if section == 'public':
            public_members[typename] = param_name
        elif section == 'private':
            private_members[typename] = param_name
    
def generate_methods(section):
    for i in range(METHODS_COUNT):
        tokens = randint(1, 4)
        function_name = ''
        for j in range(tokens):
            TOKEN_LENGTH = randint(4, 8)
            token_name = ''.join(choice(letters_low) for i in range(TOKEN_LENGTH))
            function_name = function_name + token_name if j == tokens-1 else function_name + token_name + '_'
            
        function_name = function_name + '_FUNCTION'
        fwrite.write('    void ' + function_name + '(')
        methods.append(function_name)

        PARAMS_COUNT = randint(0, 3)
        params = []
        for j in range(PARAMS_COUNT):
            r = randint(0, len(types)-1)
            typename = types[r]
            param_name = hungarian[r] + choice(letters_up)
            tokens = randint(1, 3)
            for k in range(tokens):
                TOKEN_LENGTH = randint(4, 8)
                uppercase_sign = choice(letters_up)
                token_name = ''.join(choice(letters_low) for i in range(TOKEN_LENGTH))
                token_name = uppercase_sign + token_name
                param_name = param_name + token_name if k == tokens-1 else param_name + token_name

            param_name = param_name + '_PARAM'

            if j == PARAMS_COUNT-1:
                fwrite.write(typename + ' ' + param_name)
            else:
                fwrite.write(typename + ' ' + param_name + ', ')

            params.append(typename + ' ' + param_name)
            
        if section == 'public':
            public_methods_params[function_name] = params
        elif section == 'private':
            private_methods_params[function_name] = params
        # print(public_methods_params)
        fwrite.write(');\n')


## PUBLIC
fwrite.write('public:\n')
generate_ctor_dtor(classname)
generate_methods('public')
fwrite.write('\n')
generate_members('public')
## PRIVATE
fwrite.write('\nprivate:\n')
generate_methods('private')
fwrite.write('\n')
generate_members('private')

fwrite.write('}\n')
fwrite.close()


fwrite = open('convention.cpp', 'w')
fwrite.write(classname + '::' + classname + '()\n{\n}\n\n')
fwrite.write('~' + classname + '::' + classname + '()\n{\n}\n\n')

for method, params in public_methods_params.items():
    fwrite.write(classname + '::' + method + '(')
    for i in range(len(params)):
        if i == len(params) - 1:
            fwrite.write(params[i])
        else:
            fwrite.write(params[i] + ', ')
    fwrite.write(')\n{\n')
    for i in range(len(params)):
        fwrite.write('    ' + params[i].split()[1] + ';\n')
    
    fwrite.write('}\n\n')

for method, params in private_methods_params.items():
    fwrite.write(classname + '::' + method + '(')
    for i in range(len(params)):
        if i == len(params) - 1:
            fwrite.write(params[i])
        else:
            fwrite.write(params[i] + ', ')
    fwrite.write(')\n{\n')
    for i in range(len(params)):
        fwrite.write('    ' + params[i].split()[1] + ';\n')
    
    fwrite.write('}\n\n')








