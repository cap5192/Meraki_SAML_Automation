import meraki
import os
from dotenv import load_dotenv

# load all environment variables
load_dotenv()


def get_orgs():
    """Gets the list of all orgs (name and id) that admin has access to"""
    orgs = []
    dict = {"id": "", "name": ""}
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.getOrganizations()

    for i in response:
        dict["id"] = i["id"]
        dict["name"] = i["name"]
        orgs.append(dict)
        dict = {"id": "", "name": ""}

    return orgs


def enable_api(org_id):
    """Enables API access for a dashboard org if it's not enabled"""
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.updateOrganization(
        org_id,
        api={'enabled': True}
    )

    print(f"API access has been enabled for organization ID {org_id}")


def check_api_enabled(org_id):
    """Checks if a dashboard org has API access enabled by returning a boolean"""
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)
    response = dashboard.organizations.getOrganization(
        org_id
    )
    return response['api']['enabled']


def check_saml(org_id):
    """ Returns a bool True or False if SAML is enabled on a dashboard organization """
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)

    response = dashboard.organizations.getOrganizationSaml(
        org_id
    )

    return response['enabled']


def enable_saml(org_id):
    """Enables SAML on a provided organization"""
    dashboard = meraki.DashboardAPI(api_key=os.environ['MERAKI_API_TOKEN'], output_log=False, print_console=False)

    response = dashboard.organizations.updateOrganizationSaml(
        org_id,
        enabled=True
    )

    print(f"Enabled SAML on organization ID {org_id}")
