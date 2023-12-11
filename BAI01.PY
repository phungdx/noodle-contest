import re
from collections import Counter

with open("BAI01.INP", "r") as file:
    content = file.read()
content = content.replace(",", ".")
content = re.sub("\s+", " ", content)
scores = content.split(" ")
scores = list(map(lambda x: float(x), scores))
num_participants = len(scores)
max_score = max(scores)
max_score_frequency = Counter(scores)[max_score]
max_score = str(max_score).replace(".", ",")

with open("BAI01.OUT", "w") as file:
    for i in [num_participants, max_score, max_score_frequency]:
        file.write(str(i) + "\n")
