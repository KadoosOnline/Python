# pathlib is the modern replacement for most of os.path.
# A Path object knows how to do almost everything by itself.
from pathlib import Path

path = Path('a.txt')

print(path.exists())
print(path.name)          # a.txt
print(path.stem)          # a
print(path.suffix)        # .txt
print(path.resolve())     # the absolute path

# Reading and writing in one line.
content = path.read_text(encoding='utf-8')
print(content)

Path('hello.txt').write_text('Written with pathlib\n', encoding='utf-8')

# '/' builds a path - much nicer than os.path.join.
data_folder = Path('demo_data')
data_folder.mkdir(exist_ok=True)
(data_folder / 'note.txt').write_text('a note\n', encoding='utf-8')

# Listing the .txt files of the current folder.
for txt_file in Path('.').glob('*.txt'):
    print(txt_file.name, txt_file.stat().st_size, 'bytes')
