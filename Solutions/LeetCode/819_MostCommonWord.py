import re
import collections
def mostCommonWord(paragraph: str, banned) -> str:
    words = [w for w in re.sub('[^\w]', ' ', paragraph.lower()).split() if w not in banned]

    Counter = collections.Counter(words)

    return Counter.most_common()[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))