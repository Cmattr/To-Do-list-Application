# Universal List
to_do_list = []
# Univeral Variables
home_selection = ""
# Functions
def add(add_task,to_do_list):
    to_do_list.append(f"{add_task}: incomplete")


def remove(remove_task, to_do_list):
    to_do_list.remove(f"{remove_task}: incomplete")


while home_selection != '5':
# User interface
    print('''Menu: 
    1. add a task
    2. View task
    3. Mark a task as complete
    4. Delete a task
    5. Quit''')
    home_selection = input("please select an option by number: ")

    if home_selection == '1':
        add_task = str(input("please enter the task you would like to add: "))
        add(add_task, to_do_list)
        print(f"{add_task} has been added to the list of task")

    elif home_selection == '2':
        print(f"your current task \n {to_do_list}")
    elif home_selection == '3':
        completed = input("please enter the task you would like to mark complete")
            
    elif home_selection == '4':
        try:
            remove_task = str(input("please enter the task you would like to remove: "))
            remove(remove_task, to_do_list)
            print(f"{remove_task} has been removed from your list of task")
        except Exception():
            print("please enter only the name of the item you would like to remove")    
    else:
        pass