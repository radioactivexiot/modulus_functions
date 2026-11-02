import math
while True:
    decision = input("Encrypt, Decrypt, Inverse (modular), Calculate or Exit? ").lower()
    if decision == "encrypt":
        p = int(input("Enter p (first prime number)= "))
        q = int(input("Enter q (second prime number)= "))
        n = p * q;
        phi_n = (p-1) * (q-1);           
        public_key = int(input(f"Enter public key (must be likely prime of {n}): "))
        message = int(input("Enter the number you want encrypted: "))
        ciphertext = (message**public_key) % n
        print(f"Your encrypted number is {ciphertext}")
    elif decision == "decrypt":
        public_key = int(input("Enter the public key (e): "))
        phi_n = int(input("Enter phi(n): "))
        while math.gcd(public_key, phi_n) != 1:
                    print("Phi(n) and the public key must have a gcd of 1.")
                    public_key = int(input("Enter the public key (e): "))
                    phi_n = int(input("Enter phi(n): "))
        encrypted_number = int(input("Enter encrypted number (C): "))
        n = int(input("Enter modulus (n): "))
        d = pow(public_key, -1, phi_n)
        original_number = (encrypted_number ** d) % n
        print(f"Your original number is {original_number}")
    elif decision == "exit":
        break
    elif decision == "inverse":
        first_number = int(input("Enter first number: "))
        modulus = int(input("Enter modulus: "))
        inverse = pow(first_number, -1, modulus)
        print(f"The inverse of {first_number} modulus {modulus} is {inverse}")
    elif decision == "calculate":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        modulus = int(input("Enter modulus: "))
        inverse = pow(second_number, -1, modulus)
        calculated_value = (first_number * inverse) % modulus
        print(f"Your final value is {calculated_value}")
    else:
        print("error")
                         
        
