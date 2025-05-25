from cat import Cat
import sys

def main():
    if len(sys.argv) >= 3:
        name = sys.argv[1]
        try:
            age = int(sys.argv[2])
        except ValueError:
            print('Age must be an integer. Using default age 1.')
            age = 1
    else:
        name = input('Enter your cat\'s name: ')
        try:
            age = int(input('Enter your cat\'s age: '))
        except ValueError:
            print('Invalid input. Using default age 1.')
            age = 1

    cat = Cat(name, age)
    cat.status()
    while True:
        print("""
What would you like to do with your cat?
1. Feed (fish/chicken/chocolate)
2. Let it sleep
3. Play (e.g., 'play yarn')
4. Celebrate Birthday
5. Show Happiness Index
6. Show Status
0. Exit
""")
        choice = input('Your choice: ').strip()

        if choice == '1':
            food = input('What do you want to feed?').strip()
            try:
                cat.eat(food)
            except Exception as e:
                print('NO', e)
        elif choice == '2':
            try:
                hours = int(input("How many hours should it sleep? "))
                cat.sleep(hours)
            except Exception as e:
                print('NO', e)
        elif choice == '3':
            command = input('Enter play command (e.g., \'play mouse\'): ')
            cat.play(command)
        elif choice == '4':
            cat.birthday()
        elif choice == '5':
            print('\nCalculating happiness index:')
            total = cat.happiness_index()
            print(f'Total Happiness Score: {total:.2f}')
        elif choice == '6':
            cat.status()
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    main()

