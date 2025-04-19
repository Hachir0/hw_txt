import os

cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as f:
    n = 0
    current_dish = "" 
    
    for line in f:
        line = line.strip() 
        
        if n > 0: 
            parts = line.split("|")  
            if len(parts) >= 3: 
                cook_book[current_dish].append({
                    "ingredient_name": parts[0].strip(), 
                    "quantity": parts[1].strip(),
                    "measure": parts[2].strip()
                })
                n -= 1
            continue
            
        if not line:  
            continue
            
        if line.isdigit():  
            n = int(line)
            continue
            
        if not any(char.isdigit() for char in line) and '|' not in line and len(line) > 1:
            current_dish = line.strip()
            cook_book[current_dish] = []
            
            
print("словарь с блюдами и ингредиентами:")
print(cook_book)

for dish in cook_book:
    print("\n" + dish + ":\n")
    print("----------")
    for ingredient in cook_book[dish]:
        print(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
        print("----------")
        

dishes = ["Омлет", "Фахитос"]
person_count = 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
            
        if dish not in cook_book:
            print(f"Блюдо {dish} не найдено в книге рецептов.")
            continue
        
        else:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient["ingredient_name"]
            
                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += int(ingredient['quantity']) * person_count
                    
                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
                
    return shop_list
                
                
print("\nСписок продуктов для приготовления выбранных блюд:")
print(get_shop_list_by_dishes(dishes, 2))
get_shop_list_by_dishes(dishes, person_count)



folder_path = 'papka' # путь к папке с файлами

dict_filename = {} # словарь для хранения информации о файлах и их количестве строк

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            dict_filename[filename] = len(file.readlines())
            
file_names = list(dict_filename.keys()); file_names.sort(key=dict_filename.get)   # Сортировка словаря по количеству строк в файлах и получение списка файлов с отсортированными именами


with open("combined_file.txt", "w", encoding="utf-8") as combined_file:
    for filename in file_names:
        file_path = os.path.join(folder_path, filename) # Получение пути к текущему файлу
        
        with open(file_path, 'r', encoding='utf-8') as infile: # Открытие текущего файла для чтения
            content = infile.read() # Чтение содержимого файла
            
            combined_file.write(f"{filename}\n{dict_filename[filename]}\n {content}\n\n")
