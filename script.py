from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks=[]
left_stack=Stack("Left")
middle_stack=Stack("Middle")
right_stack=Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)
#Set up the Game

num_disks=int(input("\nHow many disks do you want to play with ?\n"))
while num_disks<3:

    num_disks=int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disks,0,-1):
    left_stack.push(i)

num_optimal_moves=2**num_disks-1
print("\n The fastest you can solve this game is in {} moves".format(num_optimal_moves))
#Get User Input
def get_input():
    choices=[choice.get_name()[0] for choice in stacks]
    while True:

        print("Enter {} for {}".format(choices[0],stacks[0].get_name()),"Enter {} for {}".format(choices[1],stacks[1].get_name()),"Enter {} for {}".format(choices[2],stacks[2].get_name()))
        user_input=input("")
        if user_input.upper() in choices:
            return stacks[choices.index(user_input.upper())]










#Play the Game
num_user_moves=0
while right_stack.get_size() !=num_disks:

    print ("\n\n\n...Current Stacks...")
    for i in stacks:
        i.print_items()
    while True:
        print ("\nWhich stack do you want to move from?\n")
        from_stack=get_input()
        print ("\nWhich stack do you want to move to?\n")
        to_stack=get_input()
        print(from_stack.peek(),to_stack.peek())

        if from_stack.is_empty()==True:
            print ("\n\nInvalid Move. Try Again")

        elif to_stack.is_empty() or (from_stack.peek()<to_stack.peek()):
            disk=from_stack.pop()
            to_stack.push(disk)
            num_user_moves+=1
            break
        else:
            print ("\n\nInvalid Move. Try Again")


print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves,num_optimal_moves))





