from ruaccent.ruaccent import RUAccent
from russian import normalize_russian

accentizer = RUAccent()
accentizer.load(omograph_model_size='big_poetry', use_dictionary=True, tiny_mode=False, device='cuda:0')

with open('test.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text = normalize_russian(text, numbers=True, expand=True, cyrrilize=True)

print(accentizer.process_all(text))