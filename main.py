import os
import characters

class Message:
    def __init__(self, message, P, Q):
        self.message = message
        self.P = P
        self.Q = Q

    def encode(self):
        encoded_items = list()

        for value in self.message:
            encoded_items.append(
                (value ** self.E()) % self.N()
            )

        return encoded_items

    def mcd(self, num1, num2):
        if(num1 > num2):
            maj = num1
            min = num2
        else:
            maj = num2
            min = num1
        
        DEFINE = float("inf")

        trash = DEFINE
        dividend = maj
        divider = min

        while(trash is not 0):
            trash = dividend % divider
            dividend = divider
            divider = trash

        return dividend
    
    def phi(self):
        return (self.P - 1) * (self.Q - 1)

    def D(self):
        i = 1

        while(True):
            i = i + 1
            if (self.E() * i) % self.phi() is 1:
                return i

    def E(self):
        i = 2
        while True:
            if self.mcd(i, self.phi()) is 1:
                return i
            else:
                i = i + 1
    
    def N(self):
        return self.P * self.Q

    @staticmethod
    def decode(encoded, N, D):
        decoded_items = list()

        for value in encoded:
            decoded_items.append((value ** D) % N)
        
        return decoded_items

def get_max_len_in_list(list_string):
    max_numbers = 0

    for value in list_string:
        if len(str(value)) > max_numbers:
            max_numbers = len(str(value))

    return max_numbers

def format_list_to_string(message_as_list, number_of_digits_by_character_value):
    final_string = ""

    for value in message_as_list:
        missing_digits = number_of_digits_by_character_value - len(str(value))
        
        for i in range(0, missing_digits):
            final_string = final_string + "0"
        
        final_string = final_string + str(value)
    
    return final_string

def parse_formatted_string_to_list(string_message, number_of_digits_by_character_value):
    formatted_to_list = list()

    index_counter = 0
    i = 1

    while i <= len(string_message) / number_of_digits_by_character_value:
        k = 1

        temp_string_number = ""

        while k <= number_of_digits_by_character_value:
            temp_string_number = temp_string_number + string_message[index_counter]
            index_counter = index_counter + 1
            k = k + 1

        formatted_to_list.append(int(temp_string_number))

        i = i + 1

    return formatted_to_list

def copy_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def encode():
    message = input("Mensaje a codificar: ")
    no_encoded_items = list()

    for i in message:
        no_encoded_items.append(characters.find_number(i.upper()))
    
    P = int(input("Ingrese el valor P: "))
    Q = int(input("Ingrese el valor Q: "))
    
    print()

    encoded_message = Message(message=no_encoded_items, P=P, Q=Q)

    print(f"Texto codificado: {format_list_to_string(encoded_message.encode(), get_max_len_in_list(encoded_message.encode()))}")
    print(f"Texto codificado: {encoded_message.encode()}")
    print()
    print("Hemos copiado el texto codificado al portapapeles")
    #copy_to_clipboard(encoded_message.encode())
    print()

    print("Necesitarás estos datos para desencriptar la clave")
    print(f"N: {encoded_message.N()}")
    print(f"D: {encoded_message.D()}")
    print(f"Separados por: {get_max_len_in_list(encoded_message.encode())}")

def parse_to_letters(message):
    parsed_text = ""

    for value in message:
        parsed_text = parsed_text + characters.find_name(value)

    return parsed_text

def decode():
    encoded_message = list(input("Escribe el mensaje codificado: "))
    N = int(input("Escriba el valor de N: "))
    D = int(input("Escriba el valor de D: "))
    MAX = int(input("Max len: "))
    print()
    print(f"Texto decodificado en números: {Message.decode(parse_formatted_string_to_list(encoded_message, MAX), N, D)}")
    #print(f"Texto decodificado en números: {Message.decode(encoded_message, N, D)}")
    
    try:
        print(f'Texto decodificado en letras: {parse_to_letters(Message.decode(parse_formatted_string_to_list(encoded_message, MAX), N, D))}')
    except:
        print("Los valores obtenidos de la decodificación no coinciden con el vocabulario establecido")


if __name__ == '__main__':
    while True:
        print("============================================================")
        print()
        print("Que quieres hacer bro? B)")
        print("1) Codificar un mensaje")
        print("2) Decodificar un mensaje")
        print("3) Sácame de aquí uwu")
        option = int(input("Tu opción (1/2/3): "))

        print()

        if option is 1:
            encode()
        elif option is 2:
            decode()
        elif option is 3:
            print("Bye :D")
            print()
            break
        else:
            print("Oh no!, esta opción es inválida")
        
        print()