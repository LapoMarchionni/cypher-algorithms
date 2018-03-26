from ciphers.vigenere import Vigenere

ENGLISH_IC = 1.73


def banburismus(ciphertext1, ciphertext2):
    """Compare two ciphertext to see if there are repetitions between
    the two of them.
    If the repetitions are close to the expected reptetitions for H1 this
    case is selected, else the selected case is H0. 
    """
    repetitions = 0
    assert len(ciphertext1) == len(ciphertext2), (
        "Ciphertext of different lengths")
    for index in range(len(ciphertext1)):
        if ciphertext1[index] == ciphertext2[index]:
            repetitions += 1
    expect_R_H0 = len(ciphertext1) / 26.
    expect_R_H1 = ENGLISH_IC
    # check if H0 case
    if abs(expect_R_H1 - repetitions) <= 1:
        H = "H1"
        expect_R = expect_R_H1
    else:
        H = "H0"
        expect_R = expect_R_H0
    # check if H1 case
    print('--------------------------------------')
    print("Ciphertext 1: %s" % ciphertext1)
    print("Ciphertext 2: %s" % ciphertext2)
    print("Expected R: %s" % expect_R)
    print("Repetitions: %s" % repetitions)
    print("Difference: %s" % abs(expect_R - repetitions))
    print("Estimate Banburismus case: %s" % H)
    print('--------------------------------------')


def test_banburismus():
    """Test the Banburismus test with two different vigenere
    ciphertext first and then with two equals.
    """
    text1 = ("Once upon a midnight dreary, while I pondered, weak and weary "
                "Over many a quaint and curious volume of forgotten lores.")
    text2 = ("While I nodded, nearly napping, suddenly there came a tapping "
             "As of some one gently rapping, rapping at my chamber door")
    vigenere1 = Vigenere(key_length=8)
    vigenere2 = Vigenere(key_length=8)

    # H1 case
    print("\nGenerated by the same cipher:")
    ciphertext1 = vigenere1.encrypt(text1)
    ciphertext2 = vigenere1.encrypt(text2)
    banburismus(ciphertext1, ciphertext2)

    # H0 case
    print("\nGenerated by the different ciphers:")
    ciphertext1 = vigenere1.encrypt(text1)
    ciphertext2 = vigenere2.encrypt(text2)
    banburismus(ciphertext1, ciphertext2)


if __name__ == "__main__":
    test_banburismus()