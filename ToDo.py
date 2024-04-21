# Universal List
to_do_list = []
# Univeral Variables
home_selection = ""
# Functions
def add(add_task,to_do_list):
    to_do_list.append(f"{add_task}: incomplete")


def remove_incomplete(remove_task, to_do_list):
    to_do_list.remove(f"{remove_task}: incomplete") 

def remove_complete(remove_task, to_do_list):
    to_do_list.remove(f"{remove_task}: complete") 




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
        completed = input("please enter the task you would like to mark complete: ")
        for i in range(len(to_do_list)):
            if to_do_list [i] == (f"{completed}: incomplete"):
                to_do_list [i] = (f"{completed}: complete")
                print('Your task has been marked as completed')         
    
    elif home_selection == '4':
            remove_task = str(input("please enter the task you would like to remove: "))
            status = str(input("please indicate if the task is complete or incomplete: "))
            if status == "incomplete":
                remove_incomplete(remove_task, to_do_list)
                print(f"{remove_task} has been removed from your list of task") 
            elif status == "complete":
                remove_complete(remove_task, to_do_list)
                print(f"{remove_task} has been reomved from your list of task")
             
    else:
        pass