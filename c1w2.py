import c1w1 as week1

def Skew(text):
  SkewVals = []
  SkewVal = 0
  SkewVals.append(SkewVal)
  dict = {"A": 0, "C": -1, "G": 1, "T": 0}
  for i, nt in enumerate(list(text)):
    SkewVal = SkewVal + dict[nt]
    SkewVals.append(SkewVal)
  return SkewVals


def MinSkewPos(text):
  SkewVals = Skew(text)
  MinSkewPos = []
  minSKew = min(SkewVals)
  for i, val in enumerate(SkewVals):
    if val==minSKew:
      MinSkewPos.append(str(i))
  return ' '.join(MinSkewPos)

def HammingDistance(p,q):
  hamDist = 0
  for i, nt in enumerate(p[::-1]):
    if(p[i]!=q[i]):
      hamDist += 1
  return hamDist

def ImmediateNeighbors(Pattern):
  Neighborhood = [Pattern]
  nt = ['A','C','G','T']
  for i in range (len(Pattern)):
    symbol = Pattern[i]
    for j in range(len(nt)):
      if nt[j] != symbol:
        PatternArry = list(Pattern)
        PatternArry[i] = nt[j]
        Neighbor = ''.join(PatternArry)
        Neighborhood.append(Neighbor) 
  return Neighborhood


def Neighbors(Pattern, d):
  nt = ['C','T','G','A']
  Neighborhood = []
  if d == 0:
    return {Pattern}
  if len(Pattern) == 1: 
    return nt
  SuffixNeighbors = Neighbors(Pattern[1:], d)
  for i, Text in enumerate(SuffixNeighbors):
      if (HammingDistance(Pattern[1:], Text) < d):
        for j in range(len(nt)):
          Neighborhood.append(nt[j] + Text)
      else:
        Neighborhood.append(Pattern[0:1] + Text)      
  return Neighborhood

def AproximatePatternStart(Pattern, Text, d):
  starts = []
  itr = len(Text) - len(Pattern) + 1
  for i in range(itr):
    if HammingDistance(Text[i: i+len(Pattern)], Pattern) <= d :
      starts.append(str(i)) 
  return ' '.join(starts)

def AproximatePatternCount(Pattern, Text, d):
  count = 0
  itr = len(Text) - len(Pattern) + 1
  for i in range(itr):
    if HammingDistance(Text[i: i+len(Pattern)], Pattern) <= d :
      count= count+1
  return count

def FrequentWordsWithMismatches(Text, k, d):
  FrequentPatterns = []
  NeighborhoodArray = []
  Index = []
  Count = []

  for i in range(len(Text) - k+1): 
    Nbrs = Neighbors(Text[i:i+k], d)
    for j, Nbr in enumerate(Nbrs):
      NeighborhoodArray.append(Nbr)

  for i in range(len(NeighborhoodArray)):
    Pattern = NeighborhoodArray[i] 
    Index.append(week1.PatternToNumber(Pattern))
    Count.append(1)

  SortedIndex = sorted(Index)

  for i in range (len(NeighborhoodArray) - 1): 
    if SortedIndex[i] == SortedIndex[i + 1]:
      Count[i + 1] = Count[i] + 1

  maxCount = max(Count)

  for i in range(len(NeighborhoodArray)):
    if Count[i] == maxCount:
      Pattern = week1.NumberToPattern(SortedIndex[i], k)
      FrequentPatterns.append(Pattern)

  return ' '.join(FrequentPatterns)

def FrequentWordsWithMismatchesRevcomp(Text, k, d):
  FrequentPatterns = []
  NeighborhoodArray = []
  Index = []
  Count = []

  for i in range(len(Text) - k+1): 
    Nbrs = Neighbors(Text[i:i+k], d)
    for j, Nbr in enumerate(Nbrs):
      NeighborhoodArray.append(Nbr)

  NeighborhoodArray = list(dict.fromkeys(NeighborhoodArray))

  for i in range(len(NeighborhoodArray)):
    Pattern = NeighborhoodArray[i] 
    Index.append(week1.PatternToNumber(Pattern))
    Count.append(AproximatePatternCount(Pattern, Text, d) + AproximatePatternCount(week1.RevComp(Pattern),Text,d))

  maxCount = max(Count)

  for i in range(len(NeighborhoodArray)):
    if Count[i] == maxCount:
      Pattern = week1.NumberToPattern(Index[i], k)
      FrequentPatterns.append(Pattern)

  return ' '.join(FrequentPatterns)