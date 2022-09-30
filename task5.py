import random

def random_carriage(coupe_amount = 9):
    """Случайным образом создает кол-во купе
    Args:
        coupe_ammout(int): купе

    Returns:
        carriage(int): вагон
    """
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 + 1):
        coupe[place] = random.choice([None, 'м', 'ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage

def print_carriage(carriage):
    """Выводит кол-во вагонов

    Args:
        carriage (int): вагон
    """
    for index, coupe in enumerate(carriage):
        print(index + 1, ':', coupe)

def empty_coupe_list(carriage):
    """Создает список полностью свободных купе
    
    Args:
        carriage (int): вагон

    Returns:
        Ответ
    """
    answer = {}
    for index, coupe in enumerate(carriage):
        if not any(coupe.values()):
            answer[index + 1] = coupe 
    return answer

    
def empty_place_list(carriage):
    """Создает список свободных мест в вагоне

    Args:
        carriage (int): вагон
    Returns:
        Ответ
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place]:
                answer.append(place)
    return answer 

def empty_lh_place_list(carrisge, low=True):
    """Создает список свободных нижних/верхних мест в вагоне
    
    Args:
        carriage (int): вагон
        low (int): высота
    
    Returns:
        Ответ
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place] and place % 2 == int(low):
                answer.append(place)
    return answer

def empty_places_in_gender_coupe(carriage, gender):
    """Создает список свободных мест в купе с исключительно женской/мужской компанией
    
    Args:
        carriage (int): вагон
        gender (int): пол
    
    Returns:
        Ответ
    """
    answer = []
    for coupe in carriage:
        answer1 = []
        for place in coupe:
            if not coupe[place]:
                answer1.append(place)
            elif coupe[place] != gender:
                break
        else:
            if len(answer1) < 4:
                answer += answer1
    return answer

carriage = random_carriage()
print_carriage(carriage) 

print('cписок полностью свободных купе')
print(empty_coupe_list(carriage))
print('список свободных мест в вагоне')
print(empty_place_list(carriage))
print('список свободных нижних мест в вагоне')
print(empty_lh_place_list(carriage))
print('список свободных верхних мест в вагоне')
print(empty_lh_place_list(carriage, False))
print('список свободных мест в купе с искоючительно мужской копманией')
print(empty_places_in_gender_coupe(carriage, 'м'))
print('список свободных мест в купе с искоючительно женской копманией')
print(empty_places_in_gender_coupe(carriage, 'ж'))