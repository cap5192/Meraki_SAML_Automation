import backend


def main():
    flag = True

    while flag is True:
        # Stores all org names and IDs
        orgs = backend.get_orgs()

        for i in orgs:

            # Checks if org has APIs enabled. If not, it enables it.
            api_check = backend.check_api_enabled(i['id'])
            if not api_check:
                backend.enable_api(i['id'])

            # Loops through orgs and finds if SAML has been enabled or not.
            x = backend.check_saml(i['id'])
            print(f"Organization Name: {i['name']}, SAML Enabled = {x}")

        # Waits for user input, if they would like to enable SAML for all of their orgs.
        response = input("Would you like to enable SAML for your orgs? Y or N, N to exit: ")
        if response.lower() == 'y':

            # If user selects yes, it enables SAML option for all of their orgs.
            for i in orgs:
                backend.enable_saml(i['id'])
        else:
            flag = False


if __name__ == '__main__':
    main()
