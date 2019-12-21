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

def StringProbability(String, k, Profile):
  ProbabilityArray = []
  for i in range(len(String)-k+1):
    Text = String[i:i+k]
    MProb = week3.MotifProbability(Text, Profile)
    ProbabilityArray.append(MProb)
  return ProbabilityArray

# def GibbsSampler(Dna, k, t, N):
#   Motifs = []
#   for  m, dna in enumerate(Dna):
#     start = random.randint(0,len(dna)-k)
#     Motifs.append(dna[start:start+k])
#   BestMotifs = Motifs
#   for j in range(1,N):
#     i = random.randint(0,t-1)
#     Motifi = Motifs.pop(i)
#     Profile = week3.Motif2Profile(Motifs)
#     # Motifi ← Profile-randomly generated k-mer in the i-th sequence
#     probArray = StringProbability(Motifi, k, Profile)
#     Randomi = RandomBiased(probArray) 
#     RandomMotifi = Motifi[Randomi:Randomi+k]
#     Motifs.insert(i,RandomMotifi)
#     score = week3.Score(Motifs)
#     if score < week3.Score(BestMotifs):
#       BestMotifs = Motifs
#   return BestMotifs, score

def GibbsSampler(Motifs, k, t, N):
  BestMotifs = Motifs
  for j in range(N):
    i = random.randint(0,t-1)
    Motifi = Motifs.pop(i)
    Profile = week3.Motif2Profile(Motifs)
    # print(Profile)
    # Motifi ← Profile-randomly generated k-mer in the i-th sequence
    probArray = StringProbability(Motifi, k, Profile)
    Randomi = RandomBiased(probArray) 
    RandomMotifi = Motifi[Randomi:Randomi+k]
    Motifs.insert(i,RandomMotifi)
    score = week3.Score(Motifs)
    if score < week3.Score(BestMotifs):
      BestMotifs = Motifs
  return BestMotifs, score

def run20(DnaTxt, k, t, N):
  Dna = DnaTxt.split(' ')
  bestScore = float("inf")
  for i in range(400):
    Motifs1, score1 = RandomizedMotifSearch(Dna, k, t)
    if score1 < bestScore:
      print('s1',score1)
      bestScore = score1
      bestMotifs = Motifs1
      Motifs2, score2 = GibbsSampler(Motifs1, k ,t, N)
      if score2 < score1:
        print('s2',score2)
        bestScore = score2
        bestMotifs = Motifs2
  # return '\n'.join(bestMotifs)
  return bestMotifs
