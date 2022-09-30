def symbol_statistics(text):
    """Возвращает статистику символв в тексте
    Args:
        text (str): 
        
    Returns:
        dict: статистика символов в виде словаря
    """

    start = {}
    for letter in text:
        letter = letter.lower()
        start[letter] = start.get(letter, 0) + 1
    return start

text = input('Input text ->')
start = symbol_statistics(text)
for symbol in sorted(start):
    print(symbol, '=', start[symbol])