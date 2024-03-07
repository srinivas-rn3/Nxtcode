import os
# Retrieve the value of an environmental variable named "MY_VARIABLE"
value = os.environ.get("OneDrive")

if value:
    print(f"Env variable OneDrive value is:'{value}'")
else:
    print("Env variable name is not found/set!!")

from dotenv import load_dotenv 

# Load environment variables from .env file 
load_dotenv()
# Retrieve the password from the environment variable
password = os.getenv('PASSWORD')

# Use the password securely in your code
print("Password:",password)