#     4. Extract Emails
# Write a program that receives a single string and extracts all email addresses from it.
# Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
#     • {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
#         ◦ Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
#         ◦ Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
#     • {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".".
#     Each word consists of only letters and can have hyphens "-" between the letters.
#         ◦ Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info",
#         "mail.softuni.org"
#         ◦ Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"


import re

pattern = r'\s(([a-z0-9]+[\-\.\_a-z]*)[@]([a-z\-]+([\.][a-z]+)+))\b'
input_line = input()
output_line = re.findall(pattern, input_line)

for email in output_line:
    print(email[0])
