# clerk.py
import io
from pathlib import Path
import collections
import re

working_dir = Path.cwd()
# sentence splitting patterns
alphabets = r"([A-Za-z])"
prefixes = r"(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = r"(Inc|Ltd|Jr|Sr|Co)"
starters = r"(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = r"([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = r"[.](com|net|org|io|gov)"
# tag removal pattern
TAG_RE = re.compile(r'<[^>]+>')

# possible image filetypes
image_extensions = ('jpg', 'png', 'bmp', 'jpeg', 'tiff')

def file_exists(filename):
    filename = Path(filename)
    return filename.exists()


def delete_file(filepath):
    data_file = Path(filepath)
    try:
        data_file.unlink()
    except IsADirectoryError as e:
        print(f'Error: {data_file} : {e.strerror}')


def get_path_list(path):
    path_list = path.split('/')
    return path_list


def get_full_path_string(path):
    """path must be a relative path starting with working directory """
    full_path = working_dir
    p_list = get_path_list(path)
    for i in p_list:
        full_path = full_path / i
    return full_path


def file_to_string(path):
    my_file = get_full_path_string(path)
    file = my_file.read_text()
    return file


def get_file_type(path):
    my_file = get_full_path_string(path)
    suffix = my_file.suffix
    return suffix[1:]


def get_file_name(path):
    return Path(path).name


def get_all_project_files(dir, types=image_extensions):
    files = []
    for extension in image_extensions:
        files += get_all_files_of_type(dir, extension)
    return files


def get_all_files_of_type(dir, filetype):
    pattern = "*." + filetype + "*"
    output = []
    files = collections.Counter(str(f) for f in Path(dir).rglob(pattern))
    output += files.keys()
    return output


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub(r"\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms+" "+starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
                  alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets +
                  "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" "+suffixes+"[.] "+starters, " \\1<stop> \\2", text)
    text = re.sub(" "+suffixes+"[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


if __name__ == "__main__":
    print("Nothing to see here...yet.")