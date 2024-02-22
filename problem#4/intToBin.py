#Name: Braden Stanfield   Lab: Fri 3
def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        #write your code
        binary_val += str(num1 % 2)
        num1 = num1 // 2
    return str(binary_val)


def string_reverse(input_string): 
    reverse_input = ''
    i = 1
   #write your for loop here
    while i < len(input_string):
        reverse_input += str(input_string[len(input_string) - i ])
        i += 1
    return str(reverse_input)

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)