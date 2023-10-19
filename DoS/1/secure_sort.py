'''
Secure compared to others as a faster sort is used and a limit on max number of
elements that can be sorted in one go is used to mitigate against DoS attack.
'''
def sort(data):
    MAX_ALLOWED_ELEMENTS = 1000

    if len(data) > MAX_ALLOWED_ELEMENTS:
        raise ValueError("Too many elements")
    data.sort()

data = [4, 2, 7, 1, 9, 3]

try:
    sort(data)
except ValueError as e:
    print(str(e))