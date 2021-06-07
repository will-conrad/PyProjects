is_started = False

while True:
    userIn = input('').lower()
    if userIn == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif userIn == 'start':
        if is_started:
            print('Car is already started')
        else:
            is_started = True
            print('Car started...Ready to go!')
    elif userIn == 'stop':
        if is_started:
            is_started = False
            print('Car stopped')
        else:
            print('Car is already stopped')
    elif userIn == 'quit':
        break
    else:
        print("I don't understand that")