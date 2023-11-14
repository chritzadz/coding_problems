import pandas as pd

data = []

while True:
    area = input("Enter item area (or 'stop' to exit): ")
    
    if area.lower() == 'stop':
        break
    
    name = input("Enter item name: ")
    quantity = input("Enter item quantity: ")
    
    data.append({'Area': area, 'Item Name': name, 'Item Quantity': quantity})

df = pd.DataFrame(data)

filename = 'item_data.xlsx'
df.to_excel(filename, index=False)

print(f"Data saved to {filename}")