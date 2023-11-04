'''
TODO: Make the function that creates the opportunity
'''

def createOpportunity(name, age, description, keywords, database):
    # This is a simple example that just prints the data to the console
    print(f"Opportunity Created:\nName: {name}\nAge: {age}\nDescription: {description}\nKeywords: {keywords}")

    mySQLCursor = database.connection.cursor()
    mySQLCursor.execute("INSERT INTO opportunities (name, age, description, keywords) VALUES (%s, %s, %s, %s)", (name, age, description, keywords))


    # Return a success message or result
    return "Opportunity created successfully"
