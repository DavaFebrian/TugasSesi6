def reverse_sentence(sentence):
    words = sentence.split()  # Pisahkan kalimat menjadi kata-kata
    reversed_words = [word[::-1] for word in words]  # Balik setiap kata
    reversed_sentence = ' '.join(reversed_words)  # Gabungkan kata-kata menjadi kalimat baru
    return reversed_sentence

# Masukkan kalimat
input_sentence = input("Masukkan kalimat: ")

# Balik kalimat dan tampilkan hasil
output_sentence = reverse_sentence(input_sentence)
print("Output:", output_sentence)


def count_vowel_occurrences(sentence):
    sentence = sentence.lower()  # Ubah kalimat menjadi lowercase
    vowels = "aeiou"  # Daftar huruf vokal
    vowel_count = {vowel: 0 for vowel in vowels}  # Inisialisasi hitungan huruf vokal

    for char in sentence:
        if char in vowels:
            vowel_count[char] += 1
    
    total_vowels = sum(vowel_count.values())
    
    return vowel_count, total_vowels

# Masukkan kalimat
input_sentence = input("Masukkan kalimat: ")

# Hitung jumlah huruf vokal dan tampilkan hasil
vowel_count, total_vowels = count_vowel_occurrences(input_sentence)
print("Output:")
for vowel, count in vowel_count.items():
    print(f"Jumlah huruf {vowel.upper()} = {count}")
print("Total jumlah huruf vokal =", total_vowels)
