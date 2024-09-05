import pickle
from src.main import penjumlahan

# Muat fungsi pengujian dari file pickle
with open('tests/tests.pickle', 'rb') as f:
    tests = pickle.load(f)

# Jalankan fungsi pengujian
for test in tests:
    try:
        test()
        print(f"{test.__name__} passed")
    except AssertionError:
        print(f"{test.__name__} failed")
