# TODO
#  - redo names.json to large block of text [x]
#  - add functionality to:
#  filter short words in json [x]
#  pick words of specified lengths in json [x]
#  randomly add a random amount of numbers/letters to beginning AND/OR end of picked word (Looks more natural just at end ) [x]
#   (alternately, do if word is x length, only add to end, y length add to beginning, z length both (scrapped)
#   with selection of what is added being the random aspect. See results?)
#  - pick between 5 or so email suffix choices for each generated selection [x]
#  - generate a much stronger password - use same process as username generation, then reverse? [] **in progress**
#  - output to file [x]

# Importing
import requests
import os
import random
import string
import json

# string of ascii letters in both upppercase & lowercase + string of digits  + spec characters
chars = string.ascii_letters + string.digits + '!@#$%^&*()'

# seed basis for random numbers
random.seed = (os.urandom(1024))

# choices for email suffix.
email_list = ['@yahoo.com', '@gmail.com',
              '@mail.com', '@outlook.com', '@aol.com']

# choices for generated password length.
password_length = [6, 7, 8, 9, 10, 11, 12]

# choices for generated extra email numbers length.
extra_length = [0, 1, 2, 3, 4]

# url to which the data will be sent.
# url = '#'

# list of text to act as the email base value.
email_text = json.loads(open('longest_text.json').read())

output_file = open('output.txt', 'a')

for email_data in email_text:
    # take a random amount of digits, at a random length between 0 and 4.
    name_extra = ''.join(random.choice(string.digits)
                         for i in range(random.choice(extra_length)))

    # lowercase values from email_text + random digits + random choice of email suffix.
    username = email_data.lower() + name_extra + random.choice(email_list)

    # random selection of upper & lower case characters/digits/special characters at a length of 6-12.
    password = ''.join(random.choice(chars)
                       for i in range(random.choice(password_length)))

    # Post to the specified url, don't redirect and pass usernames and passwords.
    # !!Need to specify the var for username and password from submission form.
    # requests.post(url, allow_redirects=False, data={
    #     '#': username,
    #     '#': password
    # })

    # Output list of usernames and passwords.
    output_file.write('\"Username:\" \'% s\' \"Password:\" \'% s\' \n' %
                      (username, password))
    print('Username: %s Password: %s' % (username, password))

# print(output_file)
