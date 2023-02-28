# Isilon-SyncIQ-Failover-Session

This Python script creates a SyncIQ session between a primary Isilon cluster and a secondary Isilon cluster, and starts the session to replicate data from the primary cluster to the secondary cluster. The script waits for the session to complete and reports the status of the session.


Update the primary_endpoint and secondary_endpoint variables to match the endpoints of your primary and secondary Isilon clusters, respectively.
Update the synciq_username and synciq_password variables to match the credentials of a SyncIQ user with permissions to create and start SyncIQ sessions.
Update the session_payload variable to set the name of the SyncIQ session, the source and destination clusters, and the SyncIQ policy to use.
