def get_password(n):
    """
    Generates a password for the given number n (from 3 to 20)

    Args:
        n (int): Number from 3 to 20

    Returns:
        str: Password for the given number n
    """
    password = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) % n == 0:
                password += str(i) + str(j)
    return password