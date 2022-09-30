import random

def create_votes(parties, people):
    """Создает список голосов
    Args:
        parties (int): партии
        people (int): люди
        
    Returns:
         result [list]
    """
    result = []
    for _ in range(people):
        vote = random.randint(0, parties) 
        result.append(vote if vote > 0 else -1)
    return result

def election_results(parties, votes):
    """Создает список партий в соответствии с убыванием количества полученных голосов и их процентным соотношением
    Args:
        parties (int): партии
        people (int): люди
        
    Returns:
         result [list]
    """
    results = {}
    for party in range(1, parties + 1):
        results[party] = votes.count(party)
    index = 0
    for party, vote_number in sorted(results.items(), key=lambda item: item[1], reverse=True):
        index += 1
        print(f'{index:>2}. Пaртия №{party:<3} | {vote_number:>8} |',
                f'{(vote_number/len(votes)*100):>10.2f}%')

votes = create_votes(10, 10000)
election_results(10, votes)