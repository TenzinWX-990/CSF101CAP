################################
# Tenzin Wangchuk
# BE in Mechanical Engineering
# 02230273
################################
# REFERENCES
# https://youtu.be/fn68QNcatfo?feature=shared
################################
# SOLUTION
# Your Solution Score:49483
# Put your number here:3
################################

def read_input():
    my_file = open('CSF101CAP/input_3_cap1.txt','r')
    return my_file

def calculate_score(point):
    score = {'B X': 1, 'C X': 2, 'A X': 3, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'C Z': 7, 'B Z': 9}
    total_score = 0
    for line in point:
        key = line.strip()
        value_in_dict = score.get(key, None)
        if value_in_dict is not None:
            total_score += value_in_dict
    print("Total score :", total_score)


calculate_score(read_input())
