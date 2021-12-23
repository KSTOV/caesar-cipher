from nltk.util import pr
from caesar_cipher.corpus_loader import name_list, word_list
import string

def encrypt(text, key):
    alphabet_low = string.ascii_lowercase
    alphabet_up = string.ascii_uppercase

    shifted_alphabet_low = alphabet_low[key:] + alphabet_low[:key]
    shifted_alphabet_up = alphabet_up[key:] + alphabet_up[:key]
    low_transform = str.maketrans(alphabet_low, shifted_alphabet_low)
    up_transform = str.maketrans(alphabet_up, shifted_alphabet_up)
    
    low_encrypted = text.translate(low_transform)
    combined_encrypted = low_encrypted.translate(up_transform)

    return combined_encrypted

def decrypt(encrypted, key):
    return encrypt(encrypted, -key)

def crack(encrypted):
    for i in range(26):
        word_count = 0
        words = encrypt(encrypted, i)
        list = words.split()
        for text in list:
            if text in name_list or text.lower() in word_list:
                word_count += 1
        
        if (word_count/len(list)) > .5:
            return " ".join(list)
    return ""
