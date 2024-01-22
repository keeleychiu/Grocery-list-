#Keeley 
#1/11/24
#To-do list

todoList = []
print("Which option would you like to choose? \n1.)Option1 = Add Item To List \n2.)Option2 = Show List, \n3.)Option3 = Mark As Complete, \n4.)Option4 = Remove Item From List, \n5.)Option5 = Exit The Program, \n6.)Option6 = Remove all tasks from list , \n7.)Option7 = Sort Items Aphebetically , \n8.)Option8 = Display Number Of Items On List")
while (1<= Option and Option <8):
    Option = int(input("Which option would you like to choose?"))
    if Option == 1:
        Item = input("What should be added to the list?")
        todoList.append(Item)
        print(todoList)
    if Option == 2:
        print(todoList)
    if Option == 3:
        Item = input("Which item would you like to mark as complete?")
        x = todoList.index(Item)
        todoList[x] = (Item + " Completed")
    if Option == 4:
        Item = input("Which item would you like to remove?")
        y = todoList.index(Item)
        todoList.pop(y)
    if Option == 5: 
        print("You have exited the program.")
    if Option == 6: 
        del todoList 
    if Option == 7: 
        Item = input("Which items do you want to sort?")
        x = todoList.sort(Item)
        print(todoList)
    if Option == 8:
        Item = input("What items are on your list?")
        x = todoList.count(Item)
    
        
         
