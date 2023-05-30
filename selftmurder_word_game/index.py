import os

main_word = input('Zadejte slovo: ')
main_word_letters_list = list(main_word)
word_spaces = 0

        

print(word_spaces)
max_try = int(input('Maximální počet pokusů: '))



used_letters = []
player_tryes = 0



word_string = []
passed_letter = []

# Kontrola pevných mezer a vypíše string pro pole
for p in range(len(main_word_letters_list)):
    if not p == '\xa0': 
        word_string.append('_')
    else:
        word_string.append('\xa0')

# Vyplní mezery:
for x in range(len(main_word_letters_list)): 
    if main_word_letters_list[x].isspace() == True:
        word_spaces += 1 
        word_string[x] = ' / '
        passed_letter.append(' / ')
        





def print_stats():
    print(len(passed_letter))
    print(f"Použitá písmena: {used_letters}")
    print(f"Pokusy: {player_tryes}/{max_try}")
    print(f'Písmena: {word_string}')



while True:
            
    print_stats()
    if player_tryes == max_try:
        print("------------------------")
        print("       Prohrál jsi      ")
        print("------------------------")
        print(f"Slovo:{main_word}      ")
        break
    if len(passed_letter) == len(main_word_letters_list):
        print("------------------------")
        print("       Vyhrál jsi  ")
        print("------------------------")
        print(f"Slovo:{main_word}      ")
        break

    my_letter = input("Zadejte písmeno: ")
    loop_letter_passed = False
    for letter_index in range(len(main_word_letters_list)):

        if loop_letter_passed == False:
            if my_letter == main_word_letters_list[letter_index]:
                print("Správně:")
                # Hledá další písmena:
                find_letters = 0
                for m_w in range(len(main_word_letters_list)):
                    if my_letter == main_word_letters_list[m_w]:
                        word_string[m_w] = my_letter
                        passed_letter.append(my_letter)
                        
                

                loop_letter_passed = True
    if loop_letter_passed == False:
        used_letters.append(my_letter)
        player_tryes += 1   

    loop_letter_passed = False
    os.system('cls')




