# Importing
import requests
import os
import random
import string
import json

# list of text to act as the email base value.
email_text = json.loads(open('medium_text.json').read())

# string of ascii letters in both upppercase & lowercase + string of digits  + spec characters
chars = string.ascii_letters + string.digits + '!?@#$%&*'

# seed basis for random numbers
random.seed = (os.urandom(1024))

# choices for email suffix.
email_list = ['@yahoo.com', '@gmail.com',
              '@mail.com', '@outlook.com', '@aol.com']

# choices for generated password length.
password_length = [6, 7, 8, 9, 10, 11, 12]

# choices for generated extra email numbers length.
extra_length = [0, 1, 2, 3, 4]


# url to which the data can be sent.
# url = '#'

# open output.txt in append mode.
output_file = open('output.txt', 'a')

for email_data in email_text:
    # choices for generated password additions
    pass_length = [1, 2, 3]

    pass_digits = ''.join(random.choice(chars)
                          for i in range(random.choice(pass_length)))

    # take a random amount of digits, at a random length between 0 and 4.
    name_digits = ''.join(random.choice(string.digits)
                          for i in range(random.choice(extra_length)))

    # additional values for randomly adding a second word to email.
    name_random = ["", random.choice(email_text), ""]

    # Strong password choice.
    strongPass = ''.join(random.choice(chars)
                         for i in range(random.choice(password_length)))

    # Realistic password generation.
    realPass = ''.join(random.choice(email_text) +
                       random.choice(name_random) + pass_digits)

    # Realistic password chance.
    passSelect = [strongPass, realPass, realPass]

    # lowercase values from email_text + random digits + random choice of email suffix.
    username = email_data.lower() + random.choice(name_random) + \
        name_digits + random.choice(email_list)

    # random selection of upper & lower case characters/digits/special characters at a length of 6-12.
    password = random.choice(passSelect)

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
