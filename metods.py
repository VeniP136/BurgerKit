import requests
#токен телеграмм бота
api_token = "скрыл"

#обрабатывает кнопки под сообщениями телеграм
def callback_handler(request): 
    callback_data = request["data"]
    print(callback_data)
    if callback_data == "выполнено":
        telegram_request("sendMessage", {"chat_id":request['message']['chat']['id'], "text": "выполнено"})
        
    elif callback_data == "не сделано":
        telegram_request("sendMessage", {"chat_id":request['message']['chat']['id'], "text": "не сделано"})
    else:
        print("необработанное callback_handler телеграм")
    return 200


#обрабатывает текстовые сообщения телеграм
def message_handler(request):
    text = request["text"]
    text = text.split(",")
    reply_markup = {"inline_keyboard": [[{"text": 'выполнено', "callback_data": "выполнено"}, {"text": 'не сделано', "callback_data": "не сделано"}]]}
    response = telegram_request("sendMessage", {"chat_id":text[0], "text": text[1], "reply_markup": reply_markup})
    print(1)
    print(response.__dict__)
    # print()
    
    return 200

#отправка запроса к телеграм
def telegram_request(method, params): 
    url = f'https://api.telegram.org/bot{api_token}/{method}'
    return requests.post(url, json = params)
