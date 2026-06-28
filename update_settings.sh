#!/bin/bash
PROJECT_ID="reaim-cloud"
# Replace 'your_user_id_here' with your actual UID
USER_ID="your_user_id_here"
DATABASE_URL="https://${PROJECT_ID}-default-rtdb.firebaseio.com"

# Toggle between true/false based on argument
NEW_SETTINGS="{\"readReceiptsEnabled\": $1}"

curl -X PATCH "${DATABASE_URL}/users/${USER_ID}.json" \
     -d "${NEW_SETTINGS}"

echo -e "\nSettings updated for user ${USER_ID} to: $1"
