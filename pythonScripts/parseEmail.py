

#so for this project we are going to  be attempting to utilize the gmail api

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd


# Load credentials from the JSON file
creds = Credentials.from_authorized_user_file('C:\\Users\\sucit\\OneDrive\\Documents\\Credentials\\qdt9ivfcu08bo8tp628cbjt0cqk5br3k.apps.googleusercontent.com.json')

# Use the credentials to authenticate with Gmail API or other services
# (actual usage depends on the specific library or tool you're using)
