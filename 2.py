first_string = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
first_string_list = first_string.split(' ')
var11 = ' '.join(first_string_list[:3])
var16 = first_string_list[2].split(':')

print(f"1.1 {var11}")
print(f"1.2 {first_string_list[4].removesuffix(':')}")
print(f"1.3 {first_string.replace('ideapad', 'PC-12092')}")
print(f"1.4 {first_string.rfind('failed')}")
print(f"1.5 {first_string.lower().count('s')}")
print(f"1.6 не могу догадаться как это сделать без цикла и фукнции sum")

second_string = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
second_string_list = second_string.split(' ')
pc_name = second_string_list[3]
svc_name = second_string_list[4].removesuffix(':')
log_date = ' '.join(second_string_list[:3])
#log_mess = ' '.join(second_string_list[5:9])
#err_mess = ' '.join(err_mess)

another_second_string_list = second_string.split(': ')
log_mess = another_second_string_list[-2]
err_mess = another_second_string_list[-1]

print(f'The PC "{pc_name}" receive message from service "{svc_name}" what says "{log_mess}" because "{err_mess}" at "{log_date}"')
'''
1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.
Нужно сформировать и вывести сообщение в таком формате:

The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>
'''
