class Submission:

    def __init__(self, name, description, dueDate, course):
        self.name = name
        self.description = description
        self.dueDate = dueDate
        self.course = course
    
    def createPage(self):
        page = open(f"website/pages/submissions/{self.name}.html", "w")
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

