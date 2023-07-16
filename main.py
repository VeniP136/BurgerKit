from fastapi import FastAPI
from metods import callback_handler, message_handler, telegram_request
from db import storage

#инициализация фастапи
app = FastAPI()

# сюда приходят запросы от telegram
@app.post("/update")
def update_tg(response: dict):
    # print(f"response приходящий когда чтото пишут боту: {response}")
    if "message" in response: #обработчик текстовых сообщений пользователя
        response = response["message"]
        message_handler(response)
    elif "callback_query" in response: #обработчик кнопок под сообщениями
        response = response["callback_query"]
        callback_handler(response)
        telegram_request("answerCallbackQuery", {"callback_query_id": str(response["id"])})
    else: #обработчик исключений
        print(f"response который не смогло обработать: {response}")
    return 200


# @app.get("/setwebhook")
# def setwebhook():
#     x = telegram_request("setWebhook", {"url":"https://bot2.workhunt.ru/update", "certificate": "123456789"})
#     return 200
