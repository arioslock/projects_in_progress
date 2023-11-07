import re
from collections import Counter
import numpy as np


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
        return [string_to_split]


def extract_string_containing_word(list_of_words: list, part_of_string: str) -> str:
    """Extract the words containg string from argument.

    This function searches through a list of words to find and return the part of string.

    Args:
        list_of_tags (list): A list of words from a tags column.
        word (str): String to look for.

    Returns:
        str: The market name containing the word "rynek." If not found, it returns an empty string.
    """
    for tag in list_of_words:
        if type(tag) == str and part_of_string in tag:
            return tag
    return ""


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
    if se.findall(subject):
        return str(se.findall(subject))
    elif se.findall(description):
        return str(se.findall(description))
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

    for word in text:
        word = re.sub('[^A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', ' ', word)
        new_subject += word

    words_temp = new_subject.split(' ')
    #words.append(filter(lambda x: len(x) >=4, words_temp))
    for word in words_temp:
        if len(word) >= 4:
            words.append(word)

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


def list_of_unique_values_and_count_of_values(input_list: list) -> [list, dict]:
    """Return a list of unique values and a dictionary of counted unique values.

    This function takes a list of values and returns a list of unique values and a dictionary with unique values as keys
    and the number of times each value occurs in the original list as values.

    Args:
        input_list (list): List of values.

    Returns:
        list: List of unique values from the given list.
        dict: Dictionary where each unique value is a key, and the corresponding value is the number of times that value occurred in the original list.
    """

    unique_values = set(input_list)
    occurrence_count = Counter(input_list)

    return list(unique_values), dict(occurrence_count)


# Funkcja sprawdza czy peirwszy elemnt tupli jest kluczem do słownika,
# jeśli tak to dodaje 0 elemnt do listy i zwraca set, który zawiera unikatowe wartości dla danego klucza

def find_all_words_matching_lemma(lemma: str ,list_of_tuple: list) -> set:
    """Return a set of words connected to a given lemma.

    This function takes a lemma and a list of tuples, checks if the second element of each tuple matches the lemma, and appends the corresponding words to a list. 
    After checking all the tuples, it returns a set of words that match the provided lemma.

    Args:
        lemma (str): The lemma for which matching words are sought.
        list_of_tuple (list): A list of tuples where the 0 element is a word, and the 1 element is the lemma matching this word.

    Returns:
        set: A set of words matching the provided lemma and lemma.
    """

    list_of_words_matching_lemma = []
    for word in list_of_tuple:
        if word[1] == lemma:
            list_of_words_matching_lemma.append(word[0])
    return set(list_of_words_matching_lemma)

def match_words_to_labels(dict_of_labels_and_lemma_keys: dict, dict_of_lemmas_and_matching_words: dict) -> (list, dict):
    """Returns a dictionary of labels and their corresponding matching words.

    This function takes two dictionaries as arguments:
    1. `dict_of_labels_and_lemma_keys`: A dictionary of labels with corresponding lemma keys representing various misspellings or variations of the labels.
    2. `dict_of_lemmas_and_matching_words`: A dictionary of lemmas with their corresponding matching words.

    The function iterates through each label in `dict_of_labels_and_lemma_keys`. For each label, it collects the corresponding lemma keys and attempts to find matching words for each lemma key in `dict_of_lemmas_and_matching_words`. The matched words are then added to a final dictionary, where the label serves as the key, and a set of unique matching words as the value.

    Additionally, the function keeps track of any lemma keys that couldn't find a match in `dict_of_lemmas_and_matching_words` and appends them to a list called `not_working_keys`.

    Args:
        dict_of_labels_and_lemma_keys (dict): A dictionary of labels with corresponding lemma keys.
        dict_of_lemmas_and_matching_words (dict): A dictionary of lemmas with their corresponding matching words.

    Returns:
        list: A list of lemma keys from the label dictionary that didn't match any lemma key in the lemma-words dictionary.
        dict: A dictionary of labels and their corresponding matching words extracted from the lemma-words dictionary.
    """
    final_dict = {}
    not_working_keys = []

    for key, values in dict_of_labels_and_lemma_keys.items():
        valid_values = [v for v in values if v is not np.nan]
        temp_vals = []

        for v in valid_values:
            try:
                temp_vals.extend(dict_of_lemmas_and_matching_words[v])
            except Exception:
                not_working_keys.append(v)

        final_dict[key] = set(temp_vals)

    return not_working_keys, final_dict


def find_label_in_list_of_words_from_title(dict_of_labels_and_matching_words: dict, list_of_words_from_title: list) -> str:
    """Finds the label matching words in the list of words from the email title and returns the final label.

    This function iterates through each element in the list of words from the email title and checks if it matches any value from the dictionary of label-words. If a match is found, it returns the corresponding label; otherwise, it returns an empty string.

    Args:
        dict_of_labels_and_matching_words (dict): A dictionary of labels and their corresponding matching words.
        list_of_words_from_title (list): A list of words from the email title.

    Returns:
        str: The final label describing the type of email, or an empty string if no match is found.
    """
    if len(list_of_words_from_title) > 0:
        for key, values in dict_of_labels_and_matching_words.items():
            for i in list_of_words_from_title:
                if i in values:
                    return key
        # else:
        #     return ""


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

