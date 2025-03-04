import unittest
from counting_sort import sortir_perhitungan

class TestCountingSort(unittest.TestCase):
    def test_array_kosong(self):
        """Menguji pengurutan array kosong."""
        self.assertEqual(sortir_perhitungan([]), [])
        
    def test_elemen_tunggal(self):
        """Menguji pengurutan array dengan satu elemen."""
        self.assertEqual(sortir_perhitungan([1]), [1])
        
    def test_array_terurut(self):
        """Menguji pengurutan array yang sudah terurut."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(sortir_perhitungan(arr), arr)
        
    def test_array_terurut_terbalik(self):
        """Menguji pengurutan array yang terurut terbalik."""
        self.assertEqual(sortir_perhitungan([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        
    def test_elemen_duplikat(self):
        """Menguji pengurutan array dengan elemen yang berulang."""
        self.assertEqual(sortir_perhitungan([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
        
    def test_bilangan_negatif(self):
        """Menguji pengurutan array dengan bilangan negatif."""
        self.assertEqual(sortir_perhitungan([-3, -1, -4, -1, -5]), [-5, -4, -3, -1, -1])
        
    def test_bilangan_campuran(self):
        """Menguji pengurutan array dengan bilangan positif dan negatif."""
        self.assertEqual(sortir_perhitungan([3, -1, 4, -1, 5, -9, 2, 6, -5]), [-9, -5, -1, -1, 2, 3, 4, 5, 6])
        
    def test_elemen_identik(self):
        """Menguji pengurutan array dengan semua elemen sama."""
        self.assertEqual(sortir_perhitungan([3, 3, 3, 3, 3]), [3, 3, 3, 3, 3])
        
    def test_array_besar(self):
        """Menguji pengurutan array yang lebih besar."""
        arr = list(range(100, 0, -1))  # 100 sampai 1
        expected = list(range(1, 101))  # 1 sampai 100
        self.assertEqual(sortir_perhitungan(arr), expected)

if __name__ == '__main__':
    unittest.main()