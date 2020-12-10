# Grab data
f = open('passwords.txt', 'r')
passwords = f.read()
f.close()

# Data into list
passwords = passwords.split('\n')


def password_philosophy():
    valid_passwords = 0
    for count,i in enumerate(passwords):
        min_index = passwords[count].index('-')
        min = int(passwords[count][0:min_index])
        max_index = passwords[count].index(' ')
        max = int(passwords[count][min_index+1:max_index])

        pw_index = passwords[count].index(': ')

        letter_check = passwords[count][max_index+1:pw_index]
        pw = passwords[count][pw_index+2:]

        letter_count = 0
        for p in pw:
            if p == letter_check:
                letter_count += 1

        # print(min, max)
        if letter_count >= min and letter_count <= max:
            valid_passwords += 1
        
    print(valid_passwords)

def password_philosophy_2():
    valid_passwords = 0
    for count,i in enumerate(passwords):
        min_index = passwords[count].index('-')
        min = int(passwords[count][0:min_index])
        max_index = passwords[count].index(' ')
        max = int(passwords[count][min_index+1:max_index])

        pw_index = passwords[count].index(': ')

        letter_check = passwords[count][max_index+1:pw_index]
        pw = passwords[count][pw_index+2:]

        if pw[min-1] == letter_check and pw[max-1] == letter_check:
            pass
        elif pw[min-1] == letter_check or pw[max-1] == letter_check:
            valid_passwords += 1
        
    print(valid_passwords)

password_philosophy_2()