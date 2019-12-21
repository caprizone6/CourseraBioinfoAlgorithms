import week1
import week2
import math

def MotifEnumeration(Dna, k, d):
  Patterns = []
  for i in range(len(Dna[0])-k+1):
    Text = Dna[0][i:i+k]
    for j, Pattern in enumerate(week2.Neighbors(Text,d)):
      count = 0
      for l, dna in enumerate(Dna):  
        if week2.AproximatePatternCount(Pattern, dna, d)>=1:
          count = count +1
        if count == len(Dna):
          Patterns.append(Pattern)    
  
  Patterns = list(dict.fromkeys(Patterns))
  return ' '.join(Patterns)

def calcEntropy(vals):
  entropy = 0
  for i,val in enumerate(vals):
    if (val != 0):
      entropy = entropy + (val * math.log2(val))

  entropy = -entropy
  return entropy

def MotifEntropy(Motifs):
  MotifEntropy = []
  for k in range(len(Motifs[0])):
    Count = {'A':0,'T':0,'G':0,'C':0}
    for i in range(len(Motifs)):
      nt = Motifs[i][k]
      Count[nt] = Count[nt]+1
    CountList = Count.values()
    Profile = [i / len(Motifs) for i in CountList]
    MotifEntropy.append(calcEntropy(Profile))

  return round(sum(MotifEntropy),4)


def DistanceBetweenPatternAndStrings(Pattern, Dna):
  k = len(Pattern)
  distance = 0
  for  i, dna in enumerate(Dna):
    hammingDistance = float("inf")
    for j in range(len(dna)-k+1):
      if hammingDistance > week2.HammingDistance(Pattern, dna[j:j+k]):
        hammingDistance = week2.HammingDistance(Pattern, dna[j:j+k])
    distance += hammingDistance
  return distance


def MedianString(DnaTxt, k):
  Dna = DnaTxt.split(' ')
  distance = float("inf")
  for i in range(4**k-1):
    Pattern = week1.NumberToPattern(i, k)
    dist = DistanceBetweenPatternAndStrings(Pattern, Dna)
    if distance > dist:
      distance = dist
      Median = []
      Median.append(Pattern)
    elif distance == dist:
      Median.append(Pattern)
  return Median

def Motif2Profile(Motifs):
  Profile = {'A':[],'C':[],'G':[],'T':[]}
  for k in range(len(Motifs[0])):
    for key in Profile:
      Profile[key].append(len(Motifs))

  for k in range(len(Motifs[0])):
    for i in range(len(Motifs)):
      nt = Motifs[i][k]
      for key in Profile:
        if key == nt:
          Profile[key][k] += 1    
        # Profile[key] = [t / len(Motifs)*2 for t in Profile[key]]
    # CountList = Count.values()
    # Profile = [i / len(Motifs) for i in CountList]
  return Profile

def Profile2Motif(Dna, k, Profile):
  Motifs = []
  for i, dna in enumerate(Dna):
    Motifs.append(MostProbableKmer(dna, k, Profile))
  return Motifs

def MotifProbability(Motif, Profile):
  probability = 1
  for i, nt in enumerate(Motif[::]):
    probability *= Profile[nt][i]
  return probability

def MostProbableKmer(Dna, k, Profile):
  probability = -1
  Pattern = []
  for i in range(len(Dna)-k+1):
    Text = Dna[i:i+k]
    MProb = MotifProbability(Text, Profile)
    if MProb > probability:
      Pattern = []
      probability = MProb
      Pattern.append(Text)
    elif MProb == probability:
      Pattern.append(Text)
  if(len(Pattern) == 0):
    Pattern.append(Dna[0:k])
  return Pattern[0]

# def Score(Motifs):
#   k = len(Motifs[0])
#   distance = float("inf")
#   for i in range(4**k-1):
#     Pattern = week1.NumberToPattern(i, k)
#     dist = DistanceBetweenPatternAndStrings(Pattern, Motifs)
#     if distance > dist:
#       distance = dist
#   return distance

def Score(Motifs):
  Profile = Motif2Profile(Motifs)
  consensus = ConsesnsusSeq(Profile)
  distance = DistanceBetweenPatternAndStrings(consensus, Motifs)
  return distance

def ConsesnsusSeq(Profile):
  consesus = []
  for i in range(len(Profile['A'])):
    freq = 0
    consesus.append('x')
    for key in Profile:
      if Profile[key][i] > freq:
        freq = Profile[key][i]
        consesus[i] = key
  return ''.join(consesus)

def GreedyMotifSearch(DnaTxt, k, t):
  Dna = DnaTxt.split(' ')
  BestMotifs = []
  for i, strand in enumerate(Dna):
    BestMotifs.append(strand[0:k])
  for i in range(len(Dna[0])-k+1):
    Motifs = []
    Motifs.append(Dna[0][i:i+k])
    for j in range(1,t):
      Profile = Motif2Profile(Motifs)
      Motifs.append(MostProbableKmer(Dna[j], k, Profile))
    if Score(Motifs) < Score(BestMotifs):
      BestMotifs = Motifs
  return '\n'.join(BestMotifs)
