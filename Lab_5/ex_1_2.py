from .ex_1_1 import process_item
# from Lab_5 import ex_1_1 si dupa ex_1_1.process_item

while True:
    print("Enter a number or q to quit: ")
    m = input()
    if m == 'q':
        break
    process_item(int(m))

