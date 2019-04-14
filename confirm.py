def confirm():
    while(True):
        proceed = input('create new recipe/ (y/n): ')
        if proceed == 'y':
            return True
        elif proceed == 'n':
            return False
        else:
            print('please input y or n')