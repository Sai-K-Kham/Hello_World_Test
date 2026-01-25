import statistics
list = []
def getEntry(prompt):
    while (entry := input(prompt)):
        try:
    entry = int(entry)
        break
    except ValueError:
        print('Invalid entry')
        continue
    return entry
def main():
    value = getEntry('Type in an integer: ')
    print(f'User typed in [{value}]')
if __name__ == '__main__':
    main()
