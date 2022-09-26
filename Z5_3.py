# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


def cod(s):
 
    coding = "" # Пустая строкаБ в которую будет записываться результат
    i = 0
    while i < len(s): # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        
        coding += str(count) + s[i] # добавляет к результату текущий символ и его количество
        i = i + 1
 
    return coding
 
f = open('Z5_3.txt','r')
text = f.readline()
print (text)

 

print(cod(text))

f = open("Z5_4.txt", "w")
f.write(cod(text))
f.close()
