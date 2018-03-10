class Tagger(object):
  def __init__(self):
    raise NotImplementedError
  def train(self):
    raise NotImplementedError
  def tag(self):
    raise NotImplementedError
  def evalue(self):
    raise NotImplementedError

class HMMTagger(Tagger):
  START = '<s>'
  STOP = '</s>'
  UNK = '<UNK>'
  def __init__(self, word_freq_threshold=5):
    Tagger.__init__(self)
    self.word_freq_threshold = word_freq_threshold
    self.word_vocab = set()
    self.tag_vocab = set()
  def _count_pair(self, word, tag):
    pass
  def _count_word(self, word):
    pass
  def _count_tag(self, tag):
    pass
  def _emit(self, word, tag):
    return self._count_pair(word, tag) / self._count_tag(tag)
  def _markov_model(self, sentence):
    pass
