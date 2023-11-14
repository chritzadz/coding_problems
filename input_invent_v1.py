import pandas as pd

ask_state = True
main_list = []

while ask_state == True:
    ask_subject = input("subject (box kain, props, game items, stationery, indofest, cooking supplies): ")
    ask_item_name = input("Enter the name of the item: ")
    ask_invent_qty = input('Enter the storage quantity of item: ')

    ask_state = input('continue y/n: ')
    if ask_state == "n":
        ask_state = False
    else:
        ask_state = True

sub_list = [ask_subject, ask_item_name, ask_invent_qty]
main_list.append(sub_list)

columns_list = ['Subject', 'Item', 'Quantity']

df = pd.DataFrame(main_list, columns=columns_list)

print(df.to_excel("excel.xlsx"))



        
        