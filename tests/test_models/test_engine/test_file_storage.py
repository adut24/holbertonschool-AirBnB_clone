#!/usr/bin/python3
"""
    Unittest for File Storage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """class Test for the FileStorage class"""

    def setUp(self):
        """Clear the file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    def test_init(self):
        """Test initialisation"""
        f = FileStorage()
        self.assertEqual(type(f), FileStorage)
        self.assertEqual({}, f._FileStorage__objects)
        self.assertEqual("file.json", f._FileStorage__file_path)

    def test_all(self):
        """Test the all function"""
        f = FileStorage()
        new_dict = f.all()
        self.assertEqual(type(new_dict), dict)
        self.assertDictEqual(new_dict, {})

    def test_new(self):
        """Test the new function"""
        model = BaseModel()
        self.assertEqual(len(FileStorage().all()), 1)
        user = User()
        self.assertEqual(len(FileStorage().all()), 2)

    def test_save(self):
        """Test the save function"""
        self.setUp()
        self.assertEqual(os.path.getsize("file.json"), 2)
        os.remove("file.json")
        model = BaseModel()
        model.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertGreater(os.path.getsize("file.json"), 2)

    def test_reload(self):
        """Test the reload function"""
        self.setUp()
        model = BaseModel()
        user = User()
        FileStorage().save()
        FileStorage._FileStorage__objects = {}
        self.assertEqual(len(FileStorage().all()), 0)
        FileStorage().reload()
        self.assertEqual(len(FileStorage().all()), 2)


if __name__ == '__main__':
    unittest.main()
