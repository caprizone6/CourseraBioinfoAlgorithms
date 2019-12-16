import week3
import random

# def RandomizedMotifSearch(Dna, k, t):
#   # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
#   bestscore = float("inf")
#   while True:
#     Motifs = []
#     for  j, dna in enumerate(Dna):
#       start = random.randint(0,len(dna)-k)
#       Motifs.append(dna[start:start+k])
#     # BestMotifs = Motifs
#     Profile = week3.Motif2Profile(Motifs)
#     Motifs = week3.Profile2Motif(Dna, k, Profile)
#     score = week3.Score(Motifs)
#     if score < bestscore:
#       print(score)
#       bestscore = score
#     else:  
#       return Motifs
  # return '\n'.join(BestMotifs)

def RandomizedMotifSearch(Dna, k, t):
  # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
  Motifs = []
  for  i, dna in enumerate(Dna):
    start = random.randint(0,len(dna)-k)
    Motifs.append(dna[start:start+k])
  BestMotifs = Motifs
  while True:
    Profile = week3.Motif2Profile(Motifs)
    Motifs = week3.Profile2Motif(Dna, k, Profile)
    score = week3.Score(Motifs)
    if score < week3.Score(BestMotifs):
      BestMotifs = Motifs
    else:  
      return BestMotifs, score

def run1000(DnaTxt, k, t):
  Dna = DnaTxt.split(' ')
  bestScore = float("inf")
  for i in range(1000):
    Motifs, score = RandomizedMotifSearch(Dna, k ,t)
    if score < bestScore:
      print(score)
      bestScore = score
      bestMotifs = Motifs
  return bestMotifs