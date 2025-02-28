# CyberSecurity_EthicalHacking

# COMPANY :  CODETECH IT SOLUTIONS
# NAME : CHAUHAN KUNDAN PRADIPBHAI
# INTERN ID : CT12ITI
# DOMAIN : CYBER SECURITY AND ETHICAL HACKING
# BATCH DURATION : 5 JAN 2024 TO MARCH 5 2024
# MENTOR NAME : NEELA SANTHOSH


# Task Description of Task 1

This Python script is designed to compute and verify the integrity of files using cryptographic hashes. It utilizes the hashlib library to generate hashes for files, enabling the detection of any changes or tampering. The script includes functions to generate file hashes, verify file integrity, and scan a directory to generate hashes for all files within it.

# Components
1. Importing Libraries
- The script starts by importing the necessary libraries. hashlib provides the hashing algorithms, and os is used for file and directory operations

2. Generating File Hash
   It takes the file path and hash algorithm (default is SHA-256) as arguments. The file is read in chunks to handle large files efficiently. The hash is computed incrementally and returned as a hexadecimal string

3. Verifying File Integrity
   It calculates the current hash using the generate_file_hash function and compares it with the provided original hash. The function returns True if the hashes match, indicating the file is intact, and False otherwise.

4. Scanning a Directory
   This function scans a directory and generates hashes for all files within it. It takes the directory path and hash algorithm as arguments. The os.walk function is used to traverse the directory recursively. For each file, the hash is computed and stored in a dictionary with the file path as the key. The function returns this dictionary containing file paths and their corresponding hashes

  
Conclusion
This script provides a basic yet powerful way to monitor file integrity by leveraging cryptographic hash functions. It can be useful for detecting unauthorized changes to files, verifying data integrity, and ensuring that files have not been tampered with. By scanning directories and verifying file hashes, you can create a simple integrity monitoring system tailored to your needs 

![Screenshot 2025-02-28 021131](https://github.com/user-attachments/assets/2879df53-02b9-4ead-87e7-1d398e2f0bd4)
![Screenshot 2025-02-28 021156](https://github.com/user-attachments/assets/567fd36b-277e-4a0f-bbec-341bd7752383)





