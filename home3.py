# task 1
def cut_func(line):
    start = len(line)//2 - 1
    end = len(line)//2 + 2
    if len(line) < 7:
        print("Error")
    else:
        print(line[start:end])
cut_func("JhonDipPeta")

# task 2
def word_count(sentence, word):
    new_list = sentence.split()
    count = 0
    for item in new_list:
        item = ''.join(x for x in item if x.isalnum())
        if item == word:
            count += 1
    print(count)
word_count("Hey guys, my name is Jack. And my, my favourite color is green", "my")

# task 3
def transfer(number):
    trans_num = int(str(number)[::-1])
    print (trans_num == number)
transfer(808)

# task 4
def del_func(line, number):
    del_letter = line[number]
    final_word = ''.join(x for x in line if x != del_letter)
    print(final_word)
del_func("cat", 0)

# task 5
def total(int1, int2):
    if int1 == 10 or int2 == 10 or int1 + int2 == 10:
        print("True")
    else:
        print("False")
total(1, 9)





