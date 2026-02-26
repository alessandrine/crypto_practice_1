import matplotlib.pyplot as plt

with open("output.txt", 'r', encoding='utf-8') as file_analysis:
    text_analysis = file_analysis.readline()
    freq_dict = dict()
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        freq_dict.setdefault(letter, text_analysis.count(letter))
    freq_dict_sorted = dict(sorted(freq_dict.items(), key=lambda item: item[-1], reverse=True))
    print(freq_dict_sorted)

'''============== УПРОЩЁННАЯ СОРТИРОВКА ==================='''
simple_freq_dict_sorted = list(freq_dict_sorted.keys())
print(simple_freq_dict_sorted)

'''============== ОТРИСОВКА ДИАГРАММЫ ==================='''
x = [letter for letter in list(freq_dict_sorted.keys())]
y = [frequency for frequency in list(freq_dict_sorted.values())]

plt.bar(x, y, label='Встречаемость')
plt.xlabel('Символ')
plt.ylabel('Количество повторений в тексте')
plt.title('Анализ на основе произведения "451 градус по Фаренгейту"')
plt.legend()
plt.show()