import csv
from itertools import combinations
from collections import Counter


class MyUtilities:
    def __init__(self):
        self.user = None
        self.welcome_text = "Hello {}! Welcome."
        self.my_lst = ["apple", "banana", "cherry"]
        self.list1 = [1, 2, 3, 4, 5, 6]
        self.list2 = [4, 5, 6, 7, 8]
        self.lst3 = [1, 2, 3, 4, 5]

    # Kullanıcının adını alarak, kişiselleştirilmiş bir karşılama mesajı gösterir.
    # Prompts the user for their name and displays a personalized greeting message.
    def personalized_greeting(self):
        self.user = input("What is your name? ")
        print(self.welcome_text.format(self.user))

    # Verilen listeyi tersten yazdırır.
    # Reverses the order of elements in a given list.
    def reverse_list_strings(self, lst):
        return lst[::-1]

    # Kullanıcıdan bir sayı alır ve sayının pozitif, negatif veya sıfır olduğunu belirler.
    # Prompts the user to enter a number and determines whether it is positive, negative, or zero.
    def check_number(self):
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is positive.")
        elif num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")

    # İki listenin ortak elemanlarını döndürür.
    # Returns the common elements between two lists.
    def common_elements(self, list1, list2):
        return list(set(list1) & set(list2))

    # CSV dosyasındaki satır sayısını hesaplar ve ekrana yazar.
    # Counts the number of rows in a CSV file and prints it to the console.
    def count_rows_in_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        print(f"The total number of rows in the file is {len(rows)}.")

    # Bir stringteki karakterlerin frekanslarını hesaplar ve sözlük olarak döndürür.
    # Computes the frequency of characters in a string and returns it as a dictionary.
    def char_frequency(self, string):
        freq = {}
        for char in string:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    # Bir metin dosyasındaki en sık kullanılan 10 kelimeyi bulur ve ekrana yazar.
    # Finds the top 10 most commonly used words in a text file and prints them to the console.
    def find_top_10_words(self):
        filename = input("Enter text file name: ")
        with open(filename, 'r') as file:
            words = file.read().split()
            word_counts = Counter(words)
            top_10_words = word_counts.most_common(10)
            for word, count in top_10_words:
                print(f"{word}: {count}")

    # Verilen listedeki elemanların tüm kombinasyonlarını bulur ve bu kombinasyonları içeren bir liste döndürür.
    # Finds all combinations of three elements in a given list and returns a list containing those combinations.
    def combinations_of_three(self, lst):
        return list(combinations(lst, 3))


if __name__ == '__main__':
    my_util = MyUtilities()

    my_util.personalized_greeting()

    print(my_util.reverse_list_strings(my_util.my_lst))

    my_util.check_number()

    print(my_util.common_elements(my_util.list1, my_util.list2))

    my_util.count_rows_in_csv("example.csv")

    string = "Hello, World!"
    print(my_util.char_frequency(string))

    my_util.find_top_10_words()

    print(my_util.combinations_of_three(my_util.lst3))