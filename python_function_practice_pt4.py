#1
def max_num(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)

#2
def mult_list(list, n=0):
    if n == len(list) - 1:
        return list[n]
    else:
        return (list[n] * mult_list(list, n+1))

#3
def rev_string(string, n=0):
    if len(string) == 0:
        return ''
    elif n == len(string) - 1:
        return string[0]
    else:
        return string[-n-1] + rev_string(string, n+1)

#4
def num_within(num, min, max):
    list = range(min, max)
    list = [*list, max]
    print(list)
    for int in list:
        if num == int:
            return True
    return False

#5
output = [[1], [1,1]]
def pascal(num):
    if num < 1:
        print("Please enter a valid number of rows")
    elif num == 1:
        print(output[0])
    else:
        row_index = 2
        while len(output) < num:
            row = []
            past_row = output[row_index - 1]
            row_length = len(past_row) + 1
            for i in range(row_length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < row_length - 1:
                    row.append(output[row_index - 1][i - 1] + output[row_index - 1][i])
                else:
                    row.append(1)
            output.append(row)
            row_index += 1
        for row in output:
            print(row)