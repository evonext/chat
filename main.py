import gpt4all

# Инициализация модели Meta-Llama-3-8B-Instruct.Q4_0
model = gpt4all.GPT4All('Meta-Llama-3-8B-Instruct.Q4_0')

# Генерация текста на основе заданного запроса
prompt = "Введите ваш запрос: "
response = model.generate(prompt)
print(response)
