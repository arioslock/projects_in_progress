import re
from collections import Counter


# split_tags
def split_string_by_char(string_to_split: str, split_char: str) -> list:
    """Split a string by a specified character and return a list of the split parts.

    Args:
        string_to_split (str): The string to be split.
        split_char (str): The character to split the string by.

    Returns:
        list: A list of split parts of the string.
    """
    try:
        split_text = string_to_split.split(f'{split_char}')
        return split_text
    except Exception:
        return (list[string_to_split])


# get_market
def extract_market_name(list_of_tags: list) -> str:
    """Extract the market name from a list of tags.

    This function searches through a list of tags to find and return the market name, if it contains the word "rynek".

    Args:
        list_of_tags (list): A list of words from a tags column.

    Returns:
        str: The market name containing the word "rynek." If not found, it returns an empty string.
    """
    for tag in list_of_tags:
        if "rynek" in tag:
            return tag
    return ""


# order_number
def extract_order_number(subject: str, description: str, pattern: str) -> str:
    """Extract an order number from the subject or description of an email.

    This function searches both the subject and description of an email for a matching regular expression pattern
    and returns the extracted order number if found.

    Args:
        subject (str): The subject of the email.
        description (str): The text in the email's description.
        pattern (str): The regular expression pattern to use for matching.

    Returns:
        str: The extracted order number if found, or an empty string if not found.
    """
    se = re.compile(pattern)
    subject = str(subject)
    description = str(description)
    if not se.findall(subject):
        return str(se.findall(description))
    elif se.findall(description):
        return str(se.findall(subject))
    else:
        return ""


def find_words_with_more_than_four_characters(text: str) -> list:
    """Find words longer than four characters in the given text.

    This function processes the input text, replacing non-letter characters (including special Polish characters) with spaces.
    It then identifies words in the cleaned text that are longer than four characters and adds them to a list.

    Args:
        text (str): The text to be processed.

    Returns:
        list: A list of words that are longer than four characters.
    """

    words = []
    new_subject = ''

    for l in text:
        l = re.sub('[^A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', l)
        new_subject += l

    words_temp = new_subject.split(' ')

    for i in words_temp:
        if len(i) >= 4:
            words.append(i)

    return words


# all_order


def get_list_of_values_from_column(list_of_values: list, new_list: list) -> list:
    """Return a list of unique values from the source list, adding them to the destination list.

    This function takes a list of values (source list), checks if each value is present in another list (destination list).
    If a value is not in the destination list, it is added to create a list of unique values.

    Args:
        list_of_values (list): The source list of values to be checked.
        new_list (list): The destination list where unique values will be added.

    Returns:
        list: A list of unique values from the source list, including any values added to the destination list.
    """

    try:
        if list_of_values[0] in new_list:
            return new_list
        else:
            new_list.append(list_of_values)
            return new_list
    except Exception:
        i =1


# Funkcja do zliczania elementów w liscie, zwraca listę unikatowych wartości i listę unikatowych wartości z informacją ile razy występowały

# count_occurrences


def count_occurrences(input_list: list) -> [list, tuple]:
    """Return list of un.

    This function take list of values, check if they are in secound given list and if not, add them.

    Args:
        input_list (list): List of values to be checked.

    Returns:
        list: List of unique vales from given list.
    """
    unique_values = set(input_list)
    occurrence_count = Counter(input_list)

    return list(unique_values), occurrence_count

# Funkcja sprawdza czy peirwszy elemnt tupli jest kluczem do słownika,
# jeśli tak to dodaje 0 elemnt do listy i zwraca set, który zawiera unikatowe wartości dla danego klucza

def find_all_values_to_dictonary (key: str ,list_of_tuple: list) -> set:
    di = []
    for i in list_of_tuple:
        if i[1] == key:
            di.append(i[0])
    return set(di)

def get_all_values (dict1: dict, dict0: dict):
    final_dict = {}
    key_lvl1 = []
    key_lvl1.append(list(dict1.keys()))
    key_lvl1 = list(chain(*key_lvl1))
    not_working_keys = []
    for i in key_lvl1:
        temp_vals = []
        temp_keys = dict1[i]
        temp_keys = [x for x in temp_keys if x is not np.nan]
        for j in temp_keys:
            try:
                temp_vals.append(list(dict0[j]))
            except Exception:
                    not_working_keys.append(j)
        temp_vals = set(item for sublist in temp_vals for item in sublist)
        final_dict[i] = temp_vals
    return not_working_keys, final_dict

def get_all_values2(dict1: dict, dict0: dict):
    final_dict = {}
    not_working_keys = []

    for key, values in dict1.items():
        valid_values = [v for v in values if v is not np.nan]
        temp_vals = []

        for v in valid_values:
            try:
                temp_vals.extend(dict0[v])
            except Exception:
                not_working_keys.append(v)

        final_dict[key] = set(temp_vals)

    return not_working_keys, final_dict

def title_classification (dict_of_words: dict, title: list) -> str:
    if len(title) > 0:
        for key, values in dict_of_words.items():
            for i in title:
                if i in values:
                    return key

def set_day_to_first_of_month(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    date_obj = date_obj.replace(day=1)
    new_date_string = date_obj.strftime("%Y-%m-%d")
    return new_date_string

REGX_URL = r"(https?://|www\.)[^\s/$.?#].[^\s]*"

def preprocessing(text):
  text = text.lower()
  text = text.replace("&quot;", '"')

  text = re.sub(REGX_URL, ' ', text)

  tokens = [token.text for token in nlp(text)]

  tokens = [t for t in tokens if
              t not in STOP_WORDS and
              t not in string.punctuation]

  tokens = [t for t in tokens if not t.isdigit()]

  return " ".join(tokens)

def convert(data, outfile):
    db = spacy.tokens.DocBin()

    for text, labels in data:
        doc = spacy.tokens.Doc(nlp.vocab, words=text.split())
        doc.cats.update(labels['cats'])
        db.add(doc)

    db.to_disk(outfile)

def predict_spaCy (text):
    preprocessed_text = preprocessing(text)
    doc = nlp(preprocessed_text)
    label = max(doc.cats, key=doc.cats.get)
    return label

 - project super
    - main
        -- jupiter.plik
    - utilities
        -- functions.py