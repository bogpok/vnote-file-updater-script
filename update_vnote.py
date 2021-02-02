'''
Программа обновления файла _vnote.json
WIP

1 что такое tags?
2 sub_directories
3 attachment_folder


'''

import os
import time
import json



def _update():
    # Функция, выполняющая обновление файла

    # print(time.gmtime(0)) # start epoch
    now = time.localtime() # time.time(), time.clock()
    all_time = '%Y-%m-%dT%H:%M:%SZ' # string format
    vnote = '_vnote.json'
    d = './files'

    now = time.strftime(all_time, now) # конвертация времени now (картеж) в формат all_time
    print(now)
    
    
    print('\n\t Обновление списка файлов {} \n'.format(vnote))
    
    # lf = os.listdir(d) # создает лист с названиями файлов в директории
    # print(lf)
    
    test_d = {}
    test_d["created_time"] = now
    test_d["files"] = []
    
    with os.scandir(d) as dir_entries:
        for entry in dir_entries: # создает объект модуля os
            
            if not entry.name == vnote:
                print(entry.name) # имя файла
                info = entry.stat() # получение атрибутов файла
                
                birth = time.strftime(all_time, time.localtime(info.st_ctime))
                custom = time.strftime(all_time, time.localtime(info.st_mtime))
                
                print(birth) # Создан                
                print(custom) # Последнее изменение               
                
                #print(info.st_file_attributes)
                
                test_d["files"].append({
                    "attachment_folder": "",
                    "attachments": [
                    ],
                    "created_time": birth,
                    "modified_time": custom,
                    "name": entry.name,
                    "tags": [
                    ]
                
                })
                
            
    with open('_vnote.json', 'w') as output:
        json.dump(test_d, output, indent = 4)
    
    
    print('\n\t Файл обновлен\n')


def main():

    do = ""    
    
    while do == "":
        do = input("\nВы точно хотите обновить файл _vnote? y/n: ")
        if do in "yesYesдаДа1у" and do != "":
            _update()
        elif do == "":
            print("Согласитесь или откажитесь!")
        else:
            print("\n\tОтказ\n")
    
    
    
if __name__ == "__main__":
    main()