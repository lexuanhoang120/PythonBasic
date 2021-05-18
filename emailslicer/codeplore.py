def main():
    # .strip()   to received
    email = input("Please enter your email address: ").strip()
    email_name, email_domain = email_process(email)
    printE(email_name, email_domain)


def email_process(email):
    email_name = email[0:email.index("@")]
    email_domain = email[email.index("@") + 1:]
    return email_name, email_domain


def printE(email_name, email_domain):
    print(f"Username is {email_name}  ; Email domain is {email_domain}")


if __name__ == "__main__":
    main()
