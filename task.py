import streamlit as st

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, tasks):
        for task in tasks:
            self.tasks.append(task)
        st.success("Tasks added successfully!")

    def view_tasks(self):
        if self.tasks:
            st.info("Your To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                st.write(f"{idx}. {task}")
        else:
            st.info("Your To-Do List is empty!")

    def complete_task(self, completed_tasks):
        if completed_tasks:
            self.tasks = [task for idx, task in enumerate(self.tasks, 1) if idx not in completed_tasks]
            st.success("Selected tasks completed successfully!")
        else:
            st.error("Please select tasks to complete!")

def add_tasks(todo_list):
    tasks = st.text_area("Enter tasks (one per line):")
    tasks = tasks.splitlines()
    if tasks:
        todo_list.add_task(tasks)
    else:
        st.error("Please enter tasks!")

def view_tasks(todo_list):
    todo_list.view_tasks()

def complete_task(todo_list):
    completed_tasks = st.multiselect("Select tasks to complete:", list(range(1, len(todo_list.tasks) + 1)))
    todo_list.complete_task(completed_tasks)

def clear_tasks(todo_list):
    todo_list.tasks = []
    st.success("All tasks cleared!")

todo_list = ToDoList()

st.title("To-Do List Application")

add_tasks(todo_list)
if st.button("View Tasks"):
    view_tasks(todo_list)
complete_task(todo_list)
if st.button("Clear All Tasks"):
    clear_tasks(todo_list)
