# todo_server.py
import http.server
import socketserver

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added to the To-Do list."

    def show_tasks(self):
        if not self.tasks:
            return "No tasks in the To-Do list."
        else:
            tasks = "\n".join([f"{i}. {task}" for i, task in enumerate(self.tasks, start=1)])
            return f"Tasks in the To-Do list:\n{tasks}"

class ToDoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/add':
            task = self.headers['task']
            response = todo_list.add_task(task)
        elif self.path == '/show':
            response = todo_list.show_tasks()
        else:
            response = "Invalid request."

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode())

if __name__ == "__main__":
    todo_list = ToDoList()
    PORT = 8080

    with socketserver.TCPServer(("", PORT), ToDoHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

