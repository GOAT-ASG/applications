def crypt(text:str,opt:str,encrypt_times:int=1,full_decrypt:bool=False,create_file_path:str=False) -> str:
    """
    Encrypts or decrypts a given text using a custom encryption method.

    Args:
        text (str | FilePath): The text or .txt file to be encrypted or decrypted.
        opt (str): The operation to perform ('e' for encryption, 'd' for decryption).

            - 'e': Encrypt the text.
            - 'd': Decrypt the text.
        encrypt_times (int, optional):

            - int: Number of times to encrypt (default is 1, max recommended is 6).
        full_decrypt (bool, optional):

            - False: Decode once.
            - True: Decode all the way back to the original text.
        create_file (Path, optional): Additional option that creates a file for the results on the given path.

    Returns:
        str: The encrypted or decrypted text.

    Examples:
        >>> customcrypt("Hello, World!", 'e')
        'Encrypted text here...'

        >>> customcrypt("Encrypted text here...", 'd')
        'Hello, World!'
    """

    def Encryption(text,times):
        full = ''
        for t in range(times):
            repeated = []
            counted = 0

            while chr(ord('∇') + counted) in text or chr(ord('∆') + counted) in text and opt == 'e':
                counted += 2
                key1, key2 = chr(ord('∇') + counted),chr(ord('∆') + counted)


            if counted == 0:
                key1, key2 = '∇','∆'

            for i in text:
                if i not in repeated:
                    positions = [str(idx) for idx, char in enumerate(text) if char == i]  # Find all positions of the character
                    full += f"{key1}{i}{key2}{key2.join(positions)}"
                    repeated.append(i)
            text = full
            full = ''
        return text
        
    def Decryption(text,style):
        while '∇' in text:
            full = text

            if full[0] == '∇':
                key1,key2 = '∇','∆'
            else:
                key1,key2 = full[0],full[2]
                        
            decrypted_text = []

            # Parse `full`
            for block in full.split(key1)[1:]:  # Skip the first empty split result
                char, *positions = block.split(key2)  # Split into character and its positions
                for pos in positions:
                    if pos == '':
                        continue
                    decrypted_text.append((int(pos), char))  # Store positions and characters as tuples

            # Sort by position to reconstruct the original text
            decrypted_text.sort(key=lambda x: x[0])

            # Join characters in order of their positions
            full = ''.join([char for _, char in decrypted_text])
            text = full
            if style == False:
                break
        return text

    def Error_check(error=None):
        if text == '':
            raise ValueError("\033[31mInput text cannot be empty.\033[0m")
        if opt != 'e' and opt != 'd':
            raise ValueError("\033[31mInvalid option. Please choose 'e' for encryption or 'd' for decryption.\033[0m")
        if type(encrypt_times) != int or type(full_decrypt) != bool or (type(create_file_path) != str and create_file_path != False):
            raise TypeError("\033[31mInvalid option. Please use the correct value types.\033[0m")                                    
        if error != None:
            raise RuntimeError(f"\033[31mFATAL ERROR: {error}\033[0m") from error

    def Check_if_file(text):
        try:
            with open(text, "r", encoding='utf-16') as file:
                text_f = file.read()
            return text_f
        except UnicodeDecodeError:
            with open(text, "r", encoding='utf-8') as file:
                text_f = file.read()
            return text_f
        except FileNotFoundError as e:
            Error_check(e)
        
    if text[-4:] == '.txt':
        text = Check_if_file(text)
    
    Error_check()

    try:
        match opt:
            case 'e': #ENCRYPTION
                result = Encryption(text,encrypt_times)

            case 'd': #DECRYPTION
                result = Decryption(text,full_decrypt) 

        if create_file_path != False:          
            with open(create_file_path, 'w', encoding='utf-16') as f:
                f.write(result)
                f.close()
    
        return result
    
    except Exception as e:
        Error_check(e)

if __name__ == "__main__":
    _text = str(input('TEXT:'))
    _mode = str(input('Encrypt or Decrypt? \033[32me/d\033[0m ')).lower()

    _result = crypt(_text,_mode ,create_file_path="Formula.txt")
    print(_result)