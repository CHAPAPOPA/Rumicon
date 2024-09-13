import re


def clean_html(html):
    """Удаляет HTML-теги из текста"""
    clean_text = re.sub(r"<.*?>", "", html)
    return clean_text


def count_words(text):
    """Подсчитывает количество слов, состоящих минимум из 3 букв"""
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text)
    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]


# Пример использования
try:
    with open("example.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    clean_text = clean_html(html_content)
    top_words = count_words(clean_text)

    print(top_words)

except FileNotFoundError:
    print(
        "Файл 'example.html' не найден. Убедитесь, что файл находится в нужной директории."
    )
