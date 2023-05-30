import os

main_word = 'ahhoj'
main_word_letters_list = list(main_word)
max_try = 5



used_letters = []
player_tryes = 0



word_string = []
passed_letter = []
for p in range(len(main_word_letters_list)):
    word_string.append('_')


def print_stats():
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
                passed_letter.append(my_letter)
                used_letters.append(my_letter)
                word_string[letter_index] = my_letter
                # Hledá další písmena:
                find_letters = 0
                for m_w in range(len(main_word_letters_list)):
                    if my_letter == main_word_letters_list[m_w]:
                        word_string[m_w] = my_letter
                        
                

                loop_letter_passed = True
    if loop_letter_passed == False:
        used_letters.append(my_letter)
        player_tryes += 1   

    loop_letter_passed = False
    os.system('cls')




