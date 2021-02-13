'''This programm is a solution
for day 6 challenges of Advent of Code 2020:
    checking custom declaration forms.

Before running this code you should copy your
input data into the clipboard'''

import pyperclip

data = pyperclip.paste()

group_answers = data.split('\r\n\r\n')

'''for the 1st task we need one function'''

def total_groups_yes(group_answers):
    '''gives the list of all unique answers per group''' 
    answers_count = []
    for group_answer in group_answers:
        answer = group_answer.replace('\r\n','')
        n = len(list(set(answer)))
        answers_count.append(n)
    return answers_count


'''for the second task we need two functions'''

def separate_groups_answers(group_answers):
    '''separates group answer into list of individual answers'''
    answers = []
    for group_answer in group_answers:
        answer = group_answer.split('\r\n')
        answers.append(answer)
    return answers

def common_one_group_yes(answer):
    '''calcilates common answers for one group'''
    if len(answer) == 1:
        return len(answer[0])
    else:
        n = 0
        for a in set(answer[0]):
            check = True
            for other_answer in answer[1:]:
                if a not in other_answer:
                    check = False
            if check:
                n += 1
        return n

def common_groups_yes(answers):
    '''gives the list of all common answers per group''' 
    answers_count = []
    for group_answer in answers:
        k = common_one_group_yes(group_answer)
        answers_count.append(k)
    return answers_count

      
        
if __name__ == "__main__":
    total_sum = sum(total_groups_yes(group_answers))
    common_sum = sum(common_groups_yes(separate_groups_answers(group_answers)))
    print('The answer for the 1st task is:', total_sum)
    print('The answer for the 2nd task is:', common_sum)

