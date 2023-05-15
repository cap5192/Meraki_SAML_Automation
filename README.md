# Meraki_SAML_Automation
This is a simple skeleton script that allows admins to apply bulk SAML configuration to the dashboard orgs.
This script will populate all dashboard orgs that an administrator has access to. 
It will be able to check if any of the orgs has APIs enabled or not, and switch it to enable if its turned off.
It will also able to apply SAML configuration from disabled to enabled per user's request.

To run this script, install dependences from the requirements.txt file. Then add your API key under .env file. 
