import sys

a = sys.argv
a_l = len(sys.argv)

if a_l < 2:
    print('Usage: ' + a[0] + ' [l33t file] [output file(a txt file, optional)]')
    exit()

if a_l >= 3:
    if a[2] == a[1]:
        print('Output file name cannot be same as input file!')
        print('Error: \'' + a[2] + '\' <-- Invalid file name!')
        exit()

def num_to_code(num):
    code = {
        0 : "nop",
        1 : "wrt",
        2 : "rd",
        3 : "if",
        4 : "eif",
        5 : "fwd",
        6 : "bak",
        7 : "inc",
        8 : "dec",
        9 : "con",
        10 : "end",
    }

    return code[num]

l33t_file = open(a[1], 'r')
l33t_whole_article = l33t_file.read()

l33t_words = l33t_whole_article.replace('\n', '').split(' ')
l33t_words_cut = []
for w in l33t_words:
    if w != '':
        l33t_words_cut.append(w)

l33t_real_code = []
l33t_real_code_array = []
l33t_real_code_tag_array = []
result = ''
i = 0

for w in l33t_words_cut:
    tempw = 0
    for c in w:
        if c.isdigit():
            tempw += int(c)
    l33t_real_code_array.append(tempw)
    '''
    if (i+1) % 10 == 0:
        if i == 0:
            l33t_real_code += num_to_code(tempw) + '\n'
            l33t_real_code_tag_array.append('code')
        else:
            if l33t_real_code_array[i-1] != 5 and l33t_real_code_array[i-1] != 6 and l33t_real_code_array[i-1] != 7 and l33t_real_code_array[i-1] != 8:
                l33t_real_code += num_to_code(tempw) + '\n'
                l33t_real_code_tag_array.append('code')
            else:
                if l33t_real_code_tag_array[i-1] == 'code':
                    l33t_real_code += str(tempw+1) + '\n'
                    l33t_real_code_tag_array.append('num')
                else:
                    l33t_real_code += num_to_code(tempw) + '\n'
                    l33t_real_code_tag_array.append('code')
    else:
        '''

    
    if i == 0:
        l33t_real_code.append(num_to_code(tempw))
        l33t_real_code_tag_array.append('code')
    else:
        if l33t_real_code_array[i-1] != 5 and l33t_real_code_array[i-1] != 6 and l33t_real_code_array[i-1] != 7 and l33t_real_code_array[i-1] != 8:
            l33t_real_code.append(num_to_code(tempw))
            l33t_real_code_tag_array.append('code')
        else:
            if l33t_real_code_tag_array[i-1] == 'code':
                l33t_real_code.append(str(tempw+1))
                l33t_real_code_tag_array.append('num')
            else:
                l33t_real_code.append(num_to_code(tempw))
                l33t_real_code_tag_array.append('code')    
    
    i += 1

if_times = 0

for j in range(0, len(l33t_real_code)):
    if l33t_real_code_array[j] == 3 and l33t_real_code_tag_array[j] == 'code':
        if_times += 1
    elif l33t_real_code_array[j] == 4 and l33t_real_code_tag_array[j] == 'code':
        if_times -= 1
    if j != len(l33t_real_code) - 1:
        if l33t_real_code_tag_array[j + 1] == 'num':
            result += l33t_real_code[j] + ' '
        else:
            result += l33t_real_code[j] + '\n'
            for k in range(if_times):
                result += '\t'
    else:
        result += l33t_real_code[j] + '\n'
        for k in range(if_times):
            result += '\t'

if a_l == 2:
    f = open('l33t_real_code.txt', 'w')
    f.write(result)
    print('Translated to real code is successful! \n' + 'l33t_real_code.txt' + ' created.')
if a_l >= 3:
    f = open(a[2], 'w')
    f.write(result)
    print('Translated to real code is successful! \n' + a[2] + ' created.')