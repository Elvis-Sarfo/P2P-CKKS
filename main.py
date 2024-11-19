import time
from ckks.ckks_decryptor import CKKSDecryptor
from ckks.ckks_encoder import CKKSEncoder
from ckks.ckks_encryptor import CKKSEncryptor
from ckks.ckks_evaluator import CKKSEvaluator
from ckks.ckks_key_generator import CKKSKeyGenerator
from ckks.ckks_parameters import CKKSParameters
from util.message import Message

from util.plaintext import Plaintext


def main():
    # Add more items to represent a longer message

    input_vector = [1, 2, 3, 4]
    print(len(input_vector))

    # Start measuring time


    _message1 = Message(input_vector)

    # Add padding to message the message to be a multiple of 2
    # padded_message1 = _message1.add_dynamic_padding()
    padded_message1 = input_vector

    start_time = time.time()
    poly_degree = len(padded_message1) << 1

    ciph_modulus = 1 << 6
    big_modulus = 1 << 12
    scaling_factor = 1 << 1
    params1 = CKKSParameters(poly_degree=poly_degree,
                            ciph_modulus=ciph_modulus,
                            big_modulus=big_modulus,
                            scaling_factor=scaling_factor)
    # End measuring time
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Parameter Setting: ", time_elapsed)

    # Start measuring time
    start_time = time.time()

    key_generator = CKKSKeyGenerator(params1)

    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Key Generation: ", time_elapsed)

    # Start measuring time
    start_time = time.time()
    public_key = key_generator.public_key
    secret_key = key_generator.secret_key
    relin_key = key_generator.relin_key
    encoder = CKKSEncoder(params1)
    encryptor = CKKSEncryptor(params1, public_key, secret_key)
    decryptor = CKKSDecryptor(params1, secret_key)
    evaluator = CKKSEvaluator(params1)


    plain1 = encoder.encode(padded_message1, scaling_factor)

    ciph1 = encryptor.encrypt(plain1)
    # End measuring time
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Encryption Time : ", time_elapsed)

    # Start measuring time
    start_time = time.time()
    decryptedPlain1 = decryptor.decrypt(ciph1)


    decoded_message = encoder.decode(decryptedPlain1)

    # remove the padding after decryption
    decoded_message = _message1.remove_padding(decoded_message)

    # End measuring time
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Decryption Time: ", time_elapsed)
    # print(decoded_message)

    ################################################################################################################################################################

    # # Add the two ciphertexts
    # ciph_sum = evaluator.add(ciph1, ciph2)

    # # Decrypt the sum
    # decrypted_sum = decryptor.decrypt(ciph_sum)

    # # Decode the decrypted sum
    # decoded_sum = encoder.decode(decrypted_sum)

    # # Remove the padding from the decoded sum
    # decoded_sum = Message.trancate_padding(decoded_sum, [_message1, _message2])

    # print(decoded_sum)

    ################################################################################################################################################################

    # # Multiply the two ciphertexts
    # ciph_product = evaluator.multiply(ciph1, ciph2, relin_key)

    # # Decrypt the product
    # decrypted_product = decryptor.decrypt(ciph_product)

    # # Decode the decrypted product
    # decoded_product = encoder.decode(decrypted_product)

    # # Remove the padding from the decoded product
    # decoded_product = Message.trancate_padding(decoded_product, messages=[_message1, _message2])

    # print(decoded_product)


if __name__ == '__main__':
    main()
