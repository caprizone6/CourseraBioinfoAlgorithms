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

def Overlap(Patterns):
  Graph = []
  Pat_size = len(Patterns)
  Pat_len = len(Patterns[0])
  for i in range(Pat_size):
    node_list = []
    node_list.append(Patterns[i])
    for j in range(Pat_size):
      if(i != j and Patterns[i][-(Pat_len-1):] == Patterns[j][0:(Pat_len-1)]):
        node_list.append(Patterns[j])
    if(len(node_list) > 1):    
      Graph.append(node_list)
  return Graph

  def runOverlap(file):
    with open(file, 'r') as file:
      Patterns = file.readlines()
    Patterns = [x.strip() for x in Patterns]
    Graph = Overlap(Patterns)
    GraphOut = []
    for i, g in enumerate(Graph):
      for j in range(len(g)):
        if j == 0:
          Connection = g[0] + ' -> '
        elif j == (len(g) - 1):
          Connection += g[j] 
        else:
          Connection += g[j] + ','
      GraphOut.append(Connection)
    return '\n'.join(GraphOut)