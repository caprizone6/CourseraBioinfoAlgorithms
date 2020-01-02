def Composition(k, Text):
  Kmers = []
  itr = len(Text) - int(k) + 1
  for i in range(itr):
    Pattern = Text[i:i+k]
    Kmers.append(Pattern)
  return '\n'.join(Kmers)

def PathToGenome(Path):
  GenomeArry = []
  Path_len = len(Path)
  for i, path in enumerate(Path):
    if (i<Path_len-1):
      if(Path[i][-(len(path)-1):] == Path[i+1][0:(len(path)-1)]):
        GenomeArry.append(path[0:1])
    else:
      GenomeArry.append(path)
  Genome = ''.join(GenomeArry)
  return Genome

def runPathToGenome(file):
  with open(file, 'r') as file:
    Path = file.readlines()
  Path = [x.strip() for x in Path]
  Genome = PathToGenome(Path)
  return Genome