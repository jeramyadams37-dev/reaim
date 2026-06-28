#!/bin/bash
# Direct API deployment using Service Account
export GOOGLE_APPLICATION_CREDENTIALS="$PWD/serviceAccountKey.json"
# We'll use the official Firebase CLI but explicitly point to the service account
# to override all cached session issues.
firebase deploy --project reaim-cloud --token "$(firebase login:ci --no-localhost | grep -o '1//.*')"
