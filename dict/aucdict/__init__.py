import re

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
        return (list[split_text])


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
def extract_order_number(subject: str, description: str, pattern: str) -> list:
    """Extract order number from subject or description.

    This function searches through subject of mail, then description, and

    Args:
        list_of_tags (list): A list of words from a tags column.

    Returns:
        str: The market name containing the word "rynek." If not found, it returns an empty string.
    """
    se = re.compile(pattern)
    subject = str(subject)
    description = str(description)
    if not se.findall(subject):
        return se.findall(description)
    elif se.findall(description):
        return se.findall(subject)
    else:
        return ""

# funkcja do tworzenia listy unikalnych wartości z kolumn. Dajemy wartość z kolumny i listę. Sprawdza czy wartość już znajduje się na liście, jeśli nie to ją dodaje

def all_order(order: list, new_list: list) -> list:
    try:
        if order[0] in new_list:
            return new_list
        else:
            new_list.append(order)
            return new_list
    except Exception:
        i =1

# trzecia funkcja do czyszczenia tytułów w celu zebrania etykiet do danych

def num_there(s):
    return any(i.isdigit() for i in s)

def find_words_with_more_than_four_characters(words_with_tags):
  words = []
  for i in words_with_tags:
    if num_there(i):
      continue
    w = re.sub('[^A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', i)
    w = w.strip(" ")
    if len(w) >= 4:
      words.append(w)

  return words

# czwarta funkcja do czyszczenia tytułów w celu zebrania etykiet do danych

def find_words_with_more_than_four_characters2(subject: str) -> list:
  words = []
  new_subject = ''
  for l in subject:
    l = re.sub('[^A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', l)
    new_subject += l
  words_temp = new_subject.split(' ')
  for i in words_temp:
    if len(i) >= 4:
      words.append(i)

  return words

# Funkcja do zliczania elementów w liscie, zwraca listę unikatowych wartości i listę unikatowych wartości z informacją ile razy występowały


def count_occurrences(input_list):
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