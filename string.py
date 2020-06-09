#https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    swapped=''
    for x in s:
        if x.islower():
            swapped=swapped+x.upper()
        else:
            swapped=swapped+x.lower()
    return swapped

#https://www.hackerrank.com/challenges/whats-your-name/problem?h_r=next-challenge&h_v=zen
def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a,b))

#https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

#https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def count_substring(string, sub_string):
    count = 0
    sub_length=len(sub_string)
    str_length=len(string)
    endIndex=str_length-sub_length
    for i in range(0, endIndex+1):
        if string[i]==sub_string[0] and string[i:i+sub_length] == sub_string:
            count=count+1
    return count