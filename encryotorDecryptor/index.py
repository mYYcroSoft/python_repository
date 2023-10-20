class encryptRailFance:
    string = ''
    number_of_rails = 0
    rails = []
    final_string = ''
    math = [0, 1, 2, 1, 0, 1, 2, 1, 0,1,2, 1, 2, 0, 1,2]
    decrypt = ''
    def __init__(self, string , number_of_rails = 3):
         self.__string = string.replace(" ", "")    
         self.__number_of_rails = number_of_rails
         self.rails = [[] for _ in range(self.__number_of_rails)]
       
    def encrypt(self):
        string_list = list(self.__string)
        for x in range(len(self.__string)):
            rail_index = self.math[x]
            self.rails[rail_index].append(string_list[x])
        
        for rail in self.rails:
            for letter in rail:
                self.final_string += letter


    

    def decrypt(self):
        rail_lengths = [len(rail) for rail in self.rails]
        decrypted_rails = [[] for _ in range(self.__number_of_rails)]
        index = 0
        for rail_index, rail_length in enumerate(rail_lengths):
            for _ in range(rail_length):
                decrypted_rails[rail_index].append(self.final_string[index])
                index += 1

        decrypted_string_list = []
        rail_index = 0
        direction = 1

        for _ in range(len(self.final_string)):
            if decrypted_rails[rail_index]:
                decrypted_string_list.append(decrypted_rails[rail_index].pop(0))
                rail_index += direction
                if rail_index == 0 or rail_index == self.__number_of_rails - 1:
                    direction *= -1
            else:
                break 
        self.__decrypt = ''.join(decrypted_string_list)


    def get_encrypt_text(self):
        return self.final_string
    def get_dencrypt_text(self):
        return self.__decrypt
    def __str__(self):
        return f'Původní string: {self.__string} O 3 kolejnicích s výstupem: {self.final_string}, Rozšifrováno: {self.__decrypt}'


string = "SVATÝKOZÁK"

encrypt_text = encryptRailFance(string)
encrypt_text.encrypt()
encrypt_text.decrypt()
print(encrypt_text)
