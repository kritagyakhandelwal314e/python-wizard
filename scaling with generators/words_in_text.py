# contains bottleneck
def words_in_text(path):
  with open(path) as handle:
    for line in handle:
      line = line.rstrip('\n')
      for word in line.split(): # bottle-neck for a very very long line
        yield word

import re
def words_in_text_scaled(path):
  BUFFER_SIZE = 2**20
  def read(): return handle.read(BUFFER_SIZE)
  def normalize(chunk): return chunk.lower().rstrip(',!.\n')
  with open(path) as handle:
    buffer = read()
    start, end = 0, -1
    while True:
      for match in re.finditer(r'[ \t\n]+', buffer):
        end = match.start()
        yield normalize(buffer[start:end])
        start = match.end()
      new_buffer = read()
      if new_buffer == '':
        break
      buffer = buffer[end+1:] + new_buffer
      start, end = 0, -1
  word = normalize(buffer[start:])

num_words = 0
for word in words_in_text('../personal_notes'):
  num_words += 1

print(num_words)

num_words = 0
for word in words_in_text_scaled('../personal_notes'):
  num_words += 1

print(num_words)