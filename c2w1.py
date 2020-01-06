def Composition(k, Text):
  Kmers = []
  itr = len(Text) - int(k) + 1
  for i in range(itr):
    Pattern = Text[i:i+k]
    Kmers.append(Pattern)
  return Kmers

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

def DeBruijn(k, Text):
  Patterns = Composition(k, Text)
  Patterns.append(Patterns[-1][1:]+'Z')
  Graph = []
  Pat_size = len(Patterns)
  Pat_len = len(Patterns[0])
  for i in range(Pat_size):
    connected_nodes = []
    origin_node = Patterns[i][:-1]
    for j in range(Pat_size):
      if(Patterns[i][-(Pat_len-1):] == Patterns[j][0:(Pat_len-1)]):
        connected_nodes.append(Patterns[j][:-1])
    if(len(connected_nodes) > 0): 
      # remove duplicate connected nodes
      connected_nodes = list(dict.fromkeys(connected_nodes)) 
      connected_nodes.sort() 
      connected_nodes.insert(0,origin_node)
      Graph.append(connected_nodes)
  Graph.sort()
  # combine adjacent nodes if origin_nodes are same
  Graph = CombineNodes(Graph)

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

def CombineNodes(Graph):
  # combine adjacent nodes if origin_nodes are same
  for i, g  in enumerate(Graph):
    if(i < len(Graph)-1 and Graph[i][0] == Graph[i+1][0]):
      Graph[i] = Graph[i] + Graph[i+1][1:]
      del Graph[i+1]
  PrimeNodeList = [Node[0] for Node in Graph]
  if(len(PrimeNodeList) != len(set(PrimeNodeList))):
    CombineNodes(Graph)
  return Graph

def Kmer2DeBruijn(Patterns):
  Graph = []
  Pat_size = len(Patterns)
  for i in range(Pat_size):
    connected_nodes = []
    origin_node = Patterns[i][:-1]
    connected_nodes.append(origin_node)
    connected_nodes.append(Patterns[i][1:])
    Graph.append(connected_nodes)
  Graph.sort()
  # combine adjacent nodes if origin_nodes are same
  Graph = CombineNodes(Graph)

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

def runKmer2DeBruijn(file):
  with open(file, 'r') as file:
    Patterns = file.readlines()
  Patterns = [x.strip() for x in Patterns]
  Graph = Kmer2DeBruijn(Patterns)
  f = open('graph.txt','w')
  f.write(Graph)
  f.close()
