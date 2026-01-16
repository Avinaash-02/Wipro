emails = list(map(str,input("Enter the Emails: ").split()))
unique_emails = open('unique_emails.txt','a')
emails = set(emails)
unique_emails.write(str(f'Unique_email : {emails}'))
