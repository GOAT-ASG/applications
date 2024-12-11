def crypt(text:str,opt:str,encrypt_times:int=1,decrypt_style:str='s',create_file:bool=False) -> str:
    """
    Encrypts or decrypts a given text using a custom encryption method.

    Args:
        text (str): The text to be encrypted or decrypted.
        opt (str): The operation to perform ('e' for encryption, 'd' for decryption).

            - 'e': Encrypt the text.
            - 'd': Decrypt the text.
        encrypt_times (int, optional): Additional option:

            - int: Number of times to encrypt (default is 1, max recommended is 6).
        decrypt_style (int, optional): Additional option:

            - str: Method for decoding (default is 's'):
            - 's': Decode once.
            - 'a': Decode all the way back to the original text.
        create_file (bool, optional): Additional option that creates a txt file for the results if True.

    Returns:
        str: The encrypted or decrypted text.

    Examples:
        >>> custom_encrypt_decrypt("Hello, World!", 'e')
        'Encrypted text here...'

        >>> custom_encrypt_decrypt("Encrypted text here...", 'd')
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
            if style == 's':
                break
        return text

    def Error_check(error=None):
        if text == '':
            raise ValueError("\033[31mInput text cannot be empty.\033[0m")
        if opt != 'e' and opt != 'd':
            raise ValueError("\033[31mInvalid option. Please choose 'e' for encryption or 'd' for decryption.\033[0m")
        if type(encrypt_times) != int or type(decrypt_style) != str or type(create_file) != bool:
            raise TypeError("\033[31mInvalid option. Please use the correct value types.\033[0m")
        if decrypt_style != 's' and decrypt_style != 'a':
            raise ValueError("\033[31mInvalid option. Please choose 's' for singular or 'a' for auto.\033[0m")                                        
        if error != None:
            raise RuntimeError(f"\033[31mFATAL ERROR: {error}\033[0m") from error

    Error_check()

    try:
        match opt:
            case 'e': #ENCRYPTION
                result = Encryption(text,encrypt_times)
                file = 'en'

            case 'd': #DECRYPTION
                result = Decryption(text,decrypt_style)
                file = 'de'   

        if create_file == True:          
            with open(f'Encoder/{file}crypted.txt', 'w', encoding='utf-16') as f:
                f.write(result)
                f.close()
    
        return result
    
    except Exception as e:
        Error_check(e)


while True:
    text = str(input('TEXT:'))
    mode = str(input('Encrypt or Decrypt? \033[32me/d\033[0m ')).lower()

    james = crypt(text,mode)
    print(james)