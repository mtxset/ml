import unittest

import FileUtils

class FileUtilsTests(unittest.TestCase):
    def test_LoadCSV(self):
        print("Testing LOADCSV")
        rows = FileUtils.LoadCSV("./Data/ex1data1.txt")
        self.assertEqual(float(rows[0][0]), 6.1101)
        self.assertEqual(float(rows[0][1]), 17.592)

    def test_ParseCSV(self):
        print("Testing ParseCSV")
        data = [['6.1101', '5.5277'], ['8.5186', '7.0032']]
        (rowsAreEqual, collumnSize, collumns, fileRows) = FileUtils.ParseCSV(data)
        self.assertTrue(rowsAreEqual)
        self.assertEqual(collumnSize, 2)
        self.assertEqual(collumns[0], ['6.1101', '8.5186'])
        self.assertEqual(collumns[1], ['5.5277', '7.0032'])

if __name__ == '__main__':
    unittest.main()