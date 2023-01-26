# 181_331_Kavallini

## Статический анализ
### Происхождение и назначение кода
Представленный кодд был реализован в рамках дисциплины «Программирование криптографических алгоритмов». Он производит шифрование и дешифрование введенного пользователем текста с помощью **Шифра вертикальной перестановки с ключ-словом**

### Результат статического анализа
В качестве статического анализатора был выбран: **PyLama**
Вывод анализатора производится в формате: *имя_файла:строка:символ_ошибки описание_ошибки [каким_инструментом_была_найдена_ошибка]*
```
main.py:1:1 W0611 'sys' imported but unused [pyflakes]
main.py:4:101 E501 line too long (171 > 100 characters) [pycodestyle]
main.py:5:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:6:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:7:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:8:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:9:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:10:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:11:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:12:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:14:1 E402 module level import not at top of file [pycodestyle]
main.py:15:1 E402 module level import not at top of file [pycodestyle]
main.py:15:26 E261 at least two spaces before inline comment [pycodestyle]
main.py:17:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:35:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:36:101 E501 line too long (130 > 100 characters) [pycodestyle]
main.py:36:31 E261 at least two spaces before inline comment [pycodestyle]
main.py:37:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:39:101 E501 line too long (124 > 100 characters) [pycodestyle]
main.py:39:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:54:101 E501 line too long (128 > 100 characters) [pycodestyle]
main.py:54:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:54:101 E261 at least two spaces before inline comment [pycodestyle]
main.py:61:32 E261 at least two spaces before inline comment [pycodestyle]
main.py:78:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:83:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:90:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:97:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:101:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:105:1 E302 expected 2 blank lines, found 1 [pycodestyle]
main.py:110:85 E261 at least two spaces before inline comment [pycodestyle]
main.py:113:101 E501 line too long (136 > 100 characters) [pycodestyle]
main.py:113:61 E262 inline comment should start with '# ' [pycodestyle]
main.py:130:40 E261 at least two spaces before inline comment [pycodestyle]
main.py:147:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:153:101 E501 line too long (118 > 100 characters) [pycodestyle]
main.py:164:101 E501 line too long (125 > 100 characters) [pycodestyle]
main.py:166:23 W292 no newline at end of file [pycodestyle]
```
Интерпретация результата:
Было найдено 38 ошибок, включая 2 предупреждения, среди них ошибки и предупреждения следующих типов:
* W0611 – указание на те импорты, которые не используются;
* E501 – слишком длинная строка;
* E402 - не все импорты находятся в верхней части модуля;
* E261 – двойной пробел перед комментарием;
* E302 – ожидалось наличие двух пустых строк после функций, но была найдена только одна;
* E262 - встроенный комментарий должен начинаться с '#';
* W292 – нет новый строки в конце файла.

### Описание проблемы и исправление
1. W0611 – указание на те импорты, которые не используются.
В данном случае импорт sys не использовался, поэтому для решения этой проблемы, достаточно было удалить или закомментировать этот импорт.

2. E402 - не все импорты находятся в верхней части модуля.
Исходный код представлен ниже:
```python
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
```
Как видно импорты math и wrap расположены после объявления переменных, хотя должны были стоять рядом с импортом random. Исправим:
```python
import random
import math
from textwrap import wrap # для шифра Плейфера и Магмы

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
```

3. E302 – ожидалось наличие двух пустых строк после функций, но была найдена только одна.
Пример такой ошибки:
```python
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):  # текст в биты
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_text(bits, encoding='utf-8', errors='surrogatepass'):  # биты в текст
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

```
Для ее решения просто добавим еще одну пустую строку между функциями.

4. W292 – нет новый строки в конце файла.
Для исправления достаточно просто добавить пустую строку в конце файла:
![image](https://user-images.githubusercontent.com/56557255/214790734-837a2d08-0f56-46b8-a73f-e8663ee2e2d4.png)

### Доказательство, что проблема исчезла
```
main.py:1:101 E501 line too long (123 > 100 characters) [pycodestyle]
main.py:1:1 E265 block comment should start with '# ' [pycodestyle]
main.py:2:1 E265 block comment should start with '# ' [pycodestyle]
main.py:3:101 E501 line too long (119 > 100 characters) [pycodestyle]
main.py:3:1 E265 block comment should start with '# ' [pycodestyle]
main.py:6:26 E261 at least two spaces before inline comment [pycodestyle]
main.py:9:101 E501 line too long (171 > 100 characters) [pycodestyle]
main.py:10:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:11:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:12:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:13:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:14:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:15:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:16:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:17:101 E501 line too long (173 > 100 characters) [pycodestyle]
main.py:19:101 E501 line too long (162 > 100 characters) [pycodestyle]
main.py:19:1 E265 block comment should start with '# ' [pycodestyle]
main.py:42:101 E501 line too long (130 > 100 characters) [pycodestyle]
main.py:42:31 E261 at least two spaces before inline comment [pycodestyle]
main.py:43:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:45:101 E501 line too long (124 > 100 characters) [pycodestyle]
main.py:45:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:61:101 E501 line too long (128 > 100 characters) [pycodestyle]
main.py:61:101 E261 at least two spaces before inline comment [pycodestyle]
main.py:68:32 E261 at least two spaces before inline comment [pycodestyle]
main.py:123:85 E261 at least two spaces before inline comment [pycodestyle]
main.py:126:101 E501 line too long (136 > 100 characters) [pycodestyle]
main.py:126:61 E262 inline comment should start with '# ' [pycodestyle]
main.py:143:40 E261 at least two spaces before inline comment [pycodestyle]
main.py:160:35 E261 at least two spaces before inline comment [pycodestyle]
main.py:166:101 E501 line too long (118 > 100 characters) [pycodestyle]
main.py:177:101 E501 line too long (125 > 100 characters) [pycodestyle]
main.py:180:101 E501 line too long (107 > 100 characters) [pycodestyle]
main.py:180:1 E265 block comment should start with '# ' [pycodestyle]
```
После сохранения изменений, описанных ранее, было найдено 34 ошибки, среди которых ошибки следующих типов:
* E501 – слишком длинная строка;
* E261 – двойной пробел перед комментарием;
* E262 - встроенный комментарий должен начинаться с '#';
* E265 – комментарий к блоку должен начинаться с '#'.
По итогу, хотя ошибки E402 и E302, а также предупреждения W0611 и W292 были иправлены, появилась новая ошибка E295, схожая с ошибкой E262.
