import os
import datetime

class Assignment:
    def __init__(self, name, dueDate, description, course):
        self.name = name
        self.dueDate = dueDate
        self.description = description
        self.course = course

    def createPage(self):
        page = open(f"website/pages/assignments/{self.name}.html", "w")
        page.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>{self.name}</title>
            <link rel="stylesheet" href="../../styles.css">
        </head>
        <body>
            <div class="header">
                <h1>{self.name}</h1>
                <h3>Due Date: {self.dueDate}</h3>
            </div>
            <div class="content">
                <p>{self.description}</p>
            </div>
            <div class="footer">
                <p>Created by: {self.course.teacher}</p>
            </div>
        </body>
        </html>
        """)
        page.close()

    def render(self):
        os.system(f"start website/pages/assignments/{self.name}.html")
    
    def submit(self, student, submission):
        page = open(f"website/pages/assignments/{self.name}/submissions/{student.name}.html", "w")
        page.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>{self.name}</title>
            <link rel="stylesheet" href="../../../../../styles.css">
        </head>
        <body>
            <div class="header">
                <h1>{self.name}</h1>
                <h3>Due Date: {self.dueDate}</h3>
            </div>
            <div class="content">
                <p>{self.description}</p>
                <p>Submission: {submission}</p>
            </div>
            <div class="footer">
                <p>Created by: {self.course.teacher}</p>
            </div>
        </body>
        </html>
        """)
        page.close()
        os.system(f"start website/pages/assignments/{self.name}/submissions/{student.name}.html")
