import week3
import random

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

def RandomBiased(Prob):
  total = sum(Prob)
  wProb = [i/total for i in Prob]
  selected = random.choices(Prob, wProb)
  i = Prob.index(selected[0])
  return i

