import os

for files in os.walk( "C:/Users/rainb/Desktop/test" ): #получение названий файлов содержащихся в директории
    for file in files:
        print( file )

i = 0
while i <= len( file ):                                #запуск цикла, подсчет количества файлов в директории для определения количества итераций
    print( "deleted ", file[i] )
    os.remove( file[i] )                               #Удаление файлов
    i += 2                                             #шаг цикла. Число указывает какой по счету файл будет удалять скрипт, если i += 1 то каждый первый, если i += 2 то каждый второй.