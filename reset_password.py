import sys
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

if len(sys.argv) != 3:
    print("Usage: python reset_password.py <screenname> <new_password>")
    sys.exit(1)

username = sys.argv[1].lower()
new_password = sys.argv[2]
email = f"{username}@reaim.app"

try:
    user = auth.get_user_by_email(email)
    auth.update_user(user.uid, password=new_password)
    print(f"✅ Password for '{username}' reset successfully.")
except auth.UserNotFoundError:
    print(f"❌ No account found for screen name '{username}'.")
except Exception as e:
    print(f"❌ Error: {e}")
