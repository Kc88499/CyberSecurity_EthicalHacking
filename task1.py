import hashlib
import os

def generate_file_hash(file_path, hash_algorithm='sha256'):
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def verify_file_integrity(file_path, original_file_hash, hash_algorithm='sha256'):
    current_file_hash = generate_file_hash(file_path, hash_algorithm)
    return current_file_hash == original_file_hash

def scan_directory(directory_path, hash_algorithm='sha256'):
    directory_hashes = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            directory_hashes[file_path] = generate_file_hash(file_path, hash_algorithm)
    return directory_hashes

file_path = 'roll.txt'
original_file_hash = generate_file_hash(file_path)
print(f'Original hash: {original_file_hash}')

# Modify the file and check integrity
is_intact = verify_file_integrity(file_path, original_file_hash)
print(f'File integrity intact: {is_intact}')

# Monitor a directory
directory_path = '/path/to/directory'
directory_hashes = scan_directory(directory_path)
for file, file_hash in directory_hashes.items():
    print(f'{file}: {file_hash}')
