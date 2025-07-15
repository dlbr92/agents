import gradio as gr
from todo_list import TodoList

# Initialize task manager
todo_list = TodoList()

def add_task(description, due_date):
    task_id = todo_list.add_task(description, due_date if due_date else None)
    return f"Task added with ID: {task_id}"

def complete_task(task_id):
    try:
        task_id = int(task_id)
        result = todo_list.complete_task(task_id)
        return "Task marked as completed." if result else "Invalid task ID."
    except ValueError:
        return "Invalid task ID."

def list_tasks():
    tasks = todo_list.list_tasks()
    if not tasks:
        return "No tasks to display."
    return "\n".join([f"ID: {task['id']}, Description: {task['description']}, Due Date: {task['due_date']}, Completed: {task['completed']}" for task in tasks])

def delete_task(task_id):
    try:
        task_id = int(task_id)
        result = todo_list.delete_task(task_id)
        return "Task deleted." if result else "Invalid task ID."
    except ValueError:
        return "Invalid task ID."

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Add Task")
            task_description = gr.Textbox(label="Task Description")
            task_due_date = gr.Textbox(label="Due Date (Optional)")
            add_button = gr.Button("Add Task")
            
        with gr.Column():
            gr.Markdown("## Complete Task")
            complete_task_id = gr.Textbox(label="Task ID")
            complete_button = gr.Button("Complete Task")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Delete Task")
            delete_task_id = gr.Textbox(label="Task ID")
            delete_button = gr.Button("Delete Task")
            
    with gr.Row():
        with gr.Column():
            gr.Markdown("## List Tasks")
            list_tasks_button = gr.Button("List All Tasks")
            tasks_output = gr.Textbox(label="Tasks", interactive=False)
    
    add_button.click(add_task, inputs=[task_description, task_due_date], outputs=task_description)
    complete_button.click(complete_task, inputs=complete_task_id, outputs=complete_task_id)
    delete_button.click(delete_task, inputs=delete_task_id, outputs=delete_task_id)
    list_tasks_button.click(list_tasks, outputs=tasks_output)

demo.launch()