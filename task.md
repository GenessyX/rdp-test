<pre>
Testcase\_#1
Отсортируйте список [-5, -23, 5, 0, 23, -6, 23, 67] без использования sort
Суммарное решение должно включать
Python3 скрипт выполняющий сортировку

Testcase\_#2
Проблема:

Корпоративный web сервер стал добавлять ругательные слова в страницы
отправляемые клиентскому устройству.

Доступ на сервер\клиент отсутствует.

Дано:
IP Сервера: ip - 192.168.255.1\ mac аа:аа:аа:аа:аа:аа
клиентский компьютер: ip - 192.168.255.2\ mac bb:bb:bb:bb:bb:bb

Устройства соеденены напрямую кабелем витая пара

Возможно поставить в разрыв между устройствами сервер (схема будет - WEB -
Сервер - Клиент)

Имена сетевых интерфейсов сервера - eth1 и еth2.
Операционная система - любой Линукс
Требуется:

Написать скрипт, выполняющий перехват трафика между устройствами и замену
ругательных слов на пробел

Суммарное решение должно включать
а) Python3 скрипт выполняющий перехват\замену.

6. Написать докер для сервера минимально возможного размера

в) Инструкции по запуску скрипта

г) файл yml для CI с проверкой корректности работы.

Testcase\_#3
Написать программу-калькулятор, которая вместо цифр и арифметических знаков принимает имена цифр\знаков:
Пример, нам необходимо посчитать 2+4:
Программе мы должны отдать строку типа: two(plus(four())) и получить ответ 6
Еще примеры:

# print(one(delit(two()))) # вывод: 0,5

# print(two(plus(four(minus(three(umnojit(two()))))))) # вывод: 0

Необходимо предусмотреть вывод для следующих цифр\знаков:
от 1 до 5 включительно
плюс, минус, умножить и делить
</pre>
