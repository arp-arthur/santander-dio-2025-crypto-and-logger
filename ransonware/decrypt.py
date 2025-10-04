from utils import KEY_FILE_NAME, retrieve_files
from cryptography.fernet import Fernet


def get_key():
    return open(KEY_FILE_NAME, 'rb').read()

def get_decrypted_content(key, content):
    return Fernet(key).decrypt(content)

def main():
    key = get_key()

    for f in retrieve_files():
        with open(f, 'rb+') as file:
            content = file.read()
            new_content = get_decrypted_content(key, content)
            file.seek(0)
            file.write(new_content)
            file.truncate()

if __name__ == '__main__':
    main()