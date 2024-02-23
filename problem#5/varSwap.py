#Name: Braden Stanfield   Lab: Fri 3
def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   a = user_val1
   b = user_val2
   c = user_val3
   d = user_val4
   user_val1 = b
   user_val2 = a
   user_val3 = d
   user_val4 = c

   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   list = swap_values(user_input1, user_input2, user_input3, user_input4)
   #print those output
   print(str(list[0]) + " " + str(list[1]) + " " + str(list[2]) + " " + str(list[3]))

 