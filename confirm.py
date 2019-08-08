def confirm(text):
    while(True):
        proceed = input(str(text) + '? (y/n): ')
        if proceed == 'y':
            return True
        elif proceed == 'n':
            return False
        else:
            print('please input y or n')