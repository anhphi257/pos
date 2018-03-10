import operator
class Counter(object):
  def __init__(self):
    self.counter = dict()
  def __getitem__(self, key):
    return self.counter[key]
  def add(self, key):
    if key in self.counter.keys():
      self.counter[key] += 1
    else:
      self.counter[key] = 1
  def keys(self):
    return self.counter.keys()
  
class DataLoader(object):
  def __init__(self):
    self.sentences = list()
    self.tag_counter = Counter()
    self._i = 0
  def load(self, filepath):
    with open(filepath) as f:
      for i, line in enumerate(f.readlines()):
        tokens = line.split()
	sentence = list()
        #print tokens
        try:
          for token in tokens:
            word, tag = token.split('/')
            #print tag
            self.tag_counter.add(tag)
            sentence.append([word, tag])
        except:
          #print 'Error at line',i,line
          pass
        self.sentences.append(sentence)
    #self.tag_counter.sort()
  def __iter__(self):
    return self
  def next(self):
    try:
      result = self.sentences[self._i]
    except IndexError:
      raise StopIteration
    self._i += 1
    return result	
  def count_tag(self):
    for tag in self.tag_counter.keys():
      print tag, self.tag_counter[tag]
def main():
  loader = DataLoader()
  loader.load('/home/student/Downloads/hmm/brown_dataset/tagged_train.txt')
  #loader.count_tag()
  print len(loader.tag_counter.keys())
  print loader.next()
if __name__ == '__main__':
  main()
