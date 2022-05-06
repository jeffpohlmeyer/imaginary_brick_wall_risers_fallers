import json


def main():
    with open('./new.json', 'r') as f:
        new_ranks = json.load(f)
    with open('./preseason.json') as f:
        old_ranks = json.load(f)
    risers_fallers = []
    for k, v in new_ranks.items():
        name = k
        rank = v.get('rank')
        change_string = ''
        if old_ranks.get(k) is not None:
            prev = old_ranks.get(k).get('rank')
            change = rank - old_ranks.get(k).get('rank')
            sign = '-' if change > 0 else '+'
            change_string = f"{sign}{abs(change)}"
        else:
            prev = 'NR'
        risers_fallers.append(f"{name}, Curr: {rank}, Prev: {prev}, Change: {change_string}")
    no_longer_ranked = []
    for k, v in old_ranks.items():
        if new_ranks.get(k) is None:
            no_longer_ranked.append(f"{k}, Prev: {v.get('rank')}")
    with open('./risers_fallers.txt', 'w') as f:
        for item in risers_fallers:
            f.write(f"{item}\n")
    with open('./no_longer_ranked.txt', 'w') as f:
        for item in no_longer_ranked:
            f.write(f"{item}\n")
    return risers_fallers, no_longer_ranked


if __name__ == '__main__':
    x, y = main()