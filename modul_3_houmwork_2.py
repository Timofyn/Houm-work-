def send_email(message, recipient, *, sender="university.help@gmail.com"):
    okonchania = ('.com', '.ru', '.net')
    if '@' not in sender or '@' not in recipient or not sender.endswith(okonchania) or \
             not recipient.endswith(okonchania):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Напоминаю самому себе о вебинаре', 'teachermail.ru', sender='teachermail.ru')
send_email('Напоминаю самому себе о вебинаре', 'teachermail.ru', sender='university.help@gmail.com')
