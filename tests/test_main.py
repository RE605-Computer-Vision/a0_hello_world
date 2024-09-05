import sys
import os

# Menambahkan folder 'src' ke PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Setelah menambahkan path, import fungsi penjumlahan
from main import penjumlahan

def test_penjumlahan():
    assert penjumlahan(2, 3) == 5
    assert penjumlahan(-1, 1) == 0
    assert penjumlahan(0, 0) == 0
    assert penjumlahan(100, 200) == 300