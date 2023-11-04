'''
TODO: Create login authentication system, integrate with microsoft
'''
import msal

# microsoft authentication stuff
CLIENT_ID = "Scholarnet"
# hiding secret key for obvious reasons
CLIENT_SECRET = "xxx"
AUTHORITY = "https://login.microsoftonline.com/common"
SCOPES = ["User.Read"]  # The scope for accessing user data

app = msal.PublicClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
)

def login():
    # logging in with microsoft
    result = app.acquire_token_silent(SCOPES, account=None)
    if not result:
        result = app.acquire_token_interactive(SCOPES)

    if "access_token" in result:
        access_token = result["access_token"]
        print("Access token:", access_token)
    else:
        print(result.get("error"))

def default_login(database):
    # need to finish implementation
    cur = database.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    print(users)
