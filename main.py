import gpt4all

# Инициализация модели Meta-Llama-3-8B-Instruct.Q4_0
model = gpt4all.GPT4All('Meta-Llama-3-8B-Instruct.Q4_0')

# Ввод многострочного запроса
print("Введите ваш запрос (напишите 'конец связи' для завершения ввода):")
lines = []
while True:
    line = input()
    if "конец связи" in line:
        break
    lines.append(line)
prompt = " ".join(lines)  # Объединяем строки пробелами

print("Запрос принят")

# Генерация текста на основе заданного запроса
response = model.generate(prompt, max_tokens=512)  # Укажите нужное количество токенов
print(response)
