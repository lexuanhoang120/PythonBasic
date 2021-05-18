from codeplore import printE, email_process


def main():
    emails = ["hoangdaik@gamil.com", "liverpoool@beccedona.com", "buocnhaycay@hcmut.edu.vn"]
    for email in emails:
        email_name, email_domain = email_process(email)
        printE(email_name, email_domain)


if __name__ == "__main__":
    main()
