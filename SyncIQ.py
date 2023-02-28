import requests
import json

# Set up the Isilon primary and secondary cluster endpoints
primary_endpoint = "https://primary.isilon.local:8080"
secondary_endpoint = "https://secondary.isilon.local:8080"

# Set up the SyncIQ session endpoint and credentials
synciq_endpoint = primary_endpoint + "/platform/3/synciq/sessions"
synciq_username = "synciq_user"
synciq_password = "synciq_password"

# Set up the SyncIQ session payload
session_payload = {
    "name": "failover_session",
    "sourceCluster": primary_endpoint,
    "destinationCluster": secondary_endpoint,
    "policy": "failover_policy"
}

# Create a new SyncIQ session
session_response = requests.post(synciq_endpoint, auth=(synciq_username, synciq_password), json=session_payload)

if session_response.status_code == 201:
    session_id = session_response.json()["id"]
    print(f"SyncIQ session created with ID: {session_id}")

    # Start the SyncIQ session
    start_session_endpoint = f"{synciq_endpoint}/{session_id}/start"
    start_session_response = requests.post(start_session_endpoint, auth=(synciq_username, synciq_password))

    if start_session_response.status_code == 200:
        print("SyncIQ session started")

        # Wait for the session to complete
        while True:
            session_status_endpoint = f"{synciq_endpoint}/{session_id}/status"
            session_status_response = requests.get(session_status_endpoint, auth=(synciq_username, synciq_password))

            if session_status_response.status_code == 200:
                session_status = session_status_response.json()["status"]

                if session_status == "success":
                    print("SyncIQ session completed successfully")
                    break
                elif session_status == "failure":
                    print("SyncIQ session failed")
                    break
                else:
                    print(f"SyncIQ session status: {session_status}")

            else:
                print(f"Failed to get SyncIQ session status: {session_status_response.status_code}")

    else:
        print(f"Failed to start SyncIQ session: {start_session_response.status_code}")
else:
    print(f"Failed to create SyncIQ session: {session_response.status_code}")
