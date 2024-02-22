#Name: Braden Stanfield   Lab: Fri 3
def feet_to_steps(user_feet):
   #write your code here
    val = int(user_feet/2.5)
    return val

if __name__ == '__main__':
    #take input feet steps here
    user_feet = float(input())
    #store it into the function
    print(feet_to_steps(user_feet))
    #print your steps here