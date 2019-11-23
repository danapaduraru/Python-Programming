from ex_1_1 import process_item

while True:
    print("Enter a number or q to quit: ")
    m = input()
    process_item(m)
    if m == 'q':
        break
