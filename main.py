import pandas as pd

TODO = "todo.csv"
COM = "complete.csv"


def load_data():
    try:
        todo_df = pd.read_csv(TODO)
    except FileNotFoundError:
        print("Todo file not found. Initializing with an empty DataFrame.")
        todo_df = pd.DataFrame(columns=['Task', 'Status'])
    except pd.errors.ParserError:  # Catch CSV parsing errors
        print("Error parsing todo.csv file.")
        todo_df = pd.DataFrame(columns=['Task', 'Status'])

    try:
        com_df = pd.read_csv(COM)
    except FileNotFoundError:
        print("Complete file not found. Initializing with an empty DataFrame.")
        com_df = pd.DataFrame(columns=['Task'])
    except pd.errors.ParserError:  # Catch CSV parsing errors
        print("Error parsing complete.csv file.")
        com_df = pd.DataFrame(columns=['Task'])

    return todo_df, com_df


def save_data(todo_df, com_df):
    todo_df.to_csv(TODO, index=False)
    com_df.to_csv(COM, index=False)


def add_task(todo_df, com_df, task):
    if todo_df is None:
        todo_df = pd.DataFrame(columns=['Task', 'Status'])
    new_task = pd.DataFrame({'Task': [task], 'Status': ['Pending']})
    todo_df = pd.concat([todo_df, new_task], ignore_index=True)
    save_data(todo_df, com_df)
    return todo_df


#The .loc function allows you to access and modify DataFrame rows by label (index).
3
def mark_task_done(todo_df, com_df, task):
    if task in todo_df['Task'].values:
        todo_df.loc[todo_df['Task'] == task, 'Status'] = "Done"
    
        com_df.loc[len(com_df)] = [task]

    else:
        print("Task not found.")
    save_data(todo_df, com_df)


def display_todo_list(todo_df):
    print("\nTO-DO List")
    print(todo_df)


def display_completed_list(com_df):
    print("\nCompleted Task List")
    print(com_df)


def main():
    todo_df, com_df = load_data()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display Todo List")
        print("4. Display Completed List")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_df = add_task(todo_df, com_df, task)
        elif choice == '2':
            task = input("Enter task to mark as done: ")
            mark_task_done(todo_df, com_df, task)
        elif choice == '3':
            display_todo_list(todo_df)
        elif choice == '4':
            display_completed_list(com_df)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


main()
