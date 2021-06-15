from translate import Translator

translator = Translator(to_lang="hi")
try:
  with open('test.txt', mode='r') as file_in:
    text = file_in.read()
    translation = translator.translate(text)
    with open('test-hi.txt', mode='w') as file_out:
      file_out.write(translation)
except FileNotFoundError as e:
  print('check file path silly!!')