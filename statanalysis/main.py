import sys
import random

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
S_blocks = [{'0': 'c', '1': '4', '2': '6', '3': '2', '4': 'a', '5': '5', '6': 'b', '7': '9', '8': 'e', '9': '8', 'a': 'd', 'b': '7', 'c': '0', 'd': '3', 'e': 'f', 'f': '1'},
            {'0': '6', '1': '8', '2': '2', '3': '3', '4': '9', '5': 'a', '6': '5', '7': 'c', '8': '1', '9': 'e', 'a': '4', 'b': '7', 'c': 'b', 'd': 'd', 'e': '0', 'f': 'f'},
            {'0': 'b', '1': '3', '2': '5', '3': '8', '4': '2', '5': 'f', '6': 'a', '7': 'd', '8': 'e', '9': '1', 'a': '7', 'b': '4', 'c': 'c', 'd': '9', 'e': '6', 'f': '0'},
            {'0': 'c', '1': '8', '2': '2', '3': '1', '4': 'd', '5': '4', '6': 'f', '7': '6', '8': '7', '9': '0', 'a': 'a', 'b': '5', 'c': '3', 'd': 'e', 'e': '9', 'f': 'b'},
            {'0': '7', '1': 'f', '2': '5', '3': 'a', '4': '8', '5': '1', '6': '6', '7': 'd', '8': '0', '9': '9', 'a': '3', 'b': 'e', 'c': 'b', 'd': '4', 'e': '2', 'f': 'c'},
            {'0': '5', '1': 'd', '2': 'f', '3': '6', '4': '9', '5': '2', '6': 'c', '7': 'a', '8': 'b', '9': '7', 'a': '8', 'b': '1', 'c': '4', 'd': '3', 'e': 'e', 'f': '0'},
            {'0': '8', '1': 'e', '2': '2', '3': '5', '4': '6', '5': '9', '6': '1', '7': 'c', '8': 'f', '9': '4', 'a': 'b', 'b': '0', 'c': 'd', 'd': 'a', 'e': '3', 'f': '7'},
            {'0': '1', '1': '7', '2': 'e', '3': 'd', '4': '0', '5': '5', '6': '8', '7': '3', '8': '4', '9': 'f', 'a': 'a', 'b': '6', 'c': '9', 'd': 'c', 'e': 'b', 'f': '2'}]
alphabet_magma = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
import math
from textwrap import wrap # для шифра Плейфера и Магмы

def create_vertical_matrix(vertical_key, original):
    column_vertical = len(vertical_key)
    row_vertical = math.ceil(len(original) / column_vertical)
    vertical_matrix = [[0] * column_vertical for i in range(row_vertical)]
    k = 0
    for i in range(len(vertical_matrix)):
        for j in range(len(vertical_matrix[i])):
            if k < len(original):
                vertical_matrix[i][j] = original[k]  # заполняем таблицу открытым текстом
            else:
                vertical_matrix[i][j] = random.choice(alphabet)
            k += 1

    for vm in vertical_matrix:
        print(vm)

    return vertical_matrix, column_vertical, row_vertical

def find_index_vertical(key):
    location_key_word = list() # исправленный порядок следования букв в ключе со значениями = местоположению в исходном ключ-слове
    array_for_minimums = list(key) # массив, нужный для удаления использованных значений

    number_index = [""] * len(key) # конвертация порядковых номеров алфавита в порядковые номера в ключ-слове по возрастанию

    n = 0
    while len(array_for_minimums) > 0:
        el = min(array_for_minimums)  # находим наименьший символ
        current_index = [i for i, d in enumerate(key) if d == el]  # получаем индексы этого символа
        location_key_word += current_index
        for c in current_index:
            number_index[c] = n
            n += 1
            array_for_minimums.remove(el)

    print(number_index)
    return location_key_word

def encrypt_or_decrypt_VERTICAL(key, vertical_matrix, column_vertical, row_vertical, it_is_encrypt): # Вертикальная перестановка

    new_matrix = [[0] * column_vertical for i in range(row_vertical)]
    new_text = ""
    j = 0
    for k in key:
        n = 0
        while n < row_vertical: # выставляем столбцы в нужном нам порядке
            if it_is_encrypt:
                new_matrix[n][j] = vertical_matrix[n][k]
            else:
                new_matrix[n][k] = vertical_matrix[n][j]
            n += 1
        j += 1
    if it_is_encrypt:
        for j in range(len(new_matrix[0])):  # считываем буквы из таблицы по столбцам
            for i in range(len(new_matrix)):
                new_text += new_matrix[i][j]
    else:
        for i in range(len(new_matrix)):  # считываем буквы из таблицы по строкам
            for j in range(len(new_matrix[i])):
                new_text += new_matrix[i][j]
    return new_text

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def change(blocks):  # меняем 16-ный код на двоичный в таблице
    for block in range(len(blocks)):
        for a in alphabet_magma:
            blocks[block][a] = from_16_to_2(blocks[block][a])
            blocks[block][from_16_to_2(a)] = blocks[block].pop(a)
    return blocks

def from_16_to_2(letter):  # переводим 16-ный символ в двоичный
    symbol = int(letter, 16)
    new_letter = bin(symbol)[2:]
    while len(new_letter) != 4:
        new_letter = "0" + new_letter
    return new_letter

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):  # текст в биты
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_text(bits, encoding='utf-8', errors='surrogatepass'):  # биты в текст
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def encrypt_or_decrypt_MAGMA(text, it_is_encrypt):  # шифр Магма
    list_for_blocks = [text[x:x + 32] for x in range(0, len(text), 32)]

    if not it_is_encrypt:
        for i in range(len(list_for_blocks)):
            list_for_blocks[i] = list_for_blocks[i][-11:] + list_for_blocks[i][:-11] # сдвиг на 11

    for i in range(len(list_for_blocks)):
        list_for_blocks[i] = wrap(list_for_blocks[i], 4)    #[list_for_blocks[i][x:x + 4] for x in range(0, len(list_for_blocks[i]), 4)]

    new_list = list()
    new_text = ""
    for block in list_for_blocks:
        i = 0
        for b in block:
            if it_is_encrypt:
                new_text += S_blocks[i][b]
            else:
                new_text += get_key(S_blocks[i], b)
            i += 1
        new_list.append(new_text)
        new_text = ""

    if it_is_encrypt:
        for i in new_list:
            new_text += i[11:] + i[:11] # сдвиг на 11
    else:
        for letter in new_list:
            new_text += letter

    return new_text


print("Введите сообщение без заглавных букв и пробелов:")
original = input()

# ВЕРТИКАЛЬНАЯ ПЕРЕСТАНОВКА
print("Введите ключ-слово:")
vertical_key = input()

vertical_matrix, column_vertical, row_vertical = create_vertical_matrix(vertical_key, original)
index_vertical_key = list()
for i in range(len(vertical_key)): # находим индекс букв ключа из алфавита
    index_vertical_key.append(alphabet.index(vertical_key[i]))
print(index_vertical_key)
location_key_word = find_index_vertical(index_vertical_key)
print(location_key_word)

encryption_text = encrypt_or_decrypt_VERTICAL(location_key_word, vertical_matrix, column_vertical, row_vertical, True)
print("Зашифрованное сообщение вертикальной перестановкой:")
print(encryption_text)

shifr_vertical_matrix = [[0] * column_vertical for i in range(row_vertical)]
n = 0
for j in range(len(shifr_vertical_matrix[0])):  # считываем буквы из матрицы по столбцам
    for i in range(len(shifr_vertical_matrix)):
        shifr_vertical_matrix[i][j] = encryption_text[n]
        n += 1

decryption_text = encrypt_or_decrypt_VERTICAL(location_key_word, shifr_vertical_matrix, column_vertical, row_vertical, False)
print("Расшифрованное сообщение вертикальной перестановкой:")
print(decryption_text)