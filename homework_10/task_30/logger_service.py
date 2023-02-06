def log_activity(message, app_data_dict):
    separator = app_data_dict["separator"]
    file = open('chat_activity_log.csv', 'a', encoding="utf-8")
    file.write(f'{app_data_dict["timeformat"]}{separator}{message.chat.username}{separator}{message.chat.id}{separator}{message.text}\n')
    file.close()