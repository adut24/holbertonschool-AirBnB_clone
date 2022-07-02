#!/usr/bin/python3
"""
    Unittest for BaseModel
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class Test for the BaseModel class"""

    def test_init(self):
        """test the constructor of BaseModel"""
        a = BaseModel()
        self.assertRegex(a.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(a.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(a.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        b = BaseModel(float("inf"))
        self.assertRegex(b.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(b.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(b.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        c = BaseModel(float("NaN"))
        self.assertRegex(c.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(c.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(c.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        d = BaseModel(4)
        self.assertRegex(d.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(d.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(d.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        e = BaseModel([1, 2, 3, 4])
        self.assertRegex(e.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(e.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(e.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        f = BaseModel({1, 2})
        self.assertRegex(f.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(f.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(f.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        g = BaseModel('Hello')
        self.assertRegex(g.id, r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}' +
                         r'-[0-9a-f]{4}-[0-9a-f]{12}')
        self.assertRegex(str(g.created_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')
        self.assertRegex(str(g.updated_at), r'20\d{2}-\d{2}-\d{2} ' +
                         r'\d{2}:\d{2}:\d{2}.\d{6}')

    def test_instantiation(self):
        """Test instantiation"""
        model = BaseModel()
        self.assertIs(type(model), BaseModel)
        self.assertIs(type(model.id), str)
        self.assertIs(type(model.created_at), datetime)
        self.assertIs(type(model.updated_at), datetime)
        model.name = "Betty"
        model.age = 100
        self.assertEqual(model.name, "Betty")
        self.assertEqual(model.age, 100)

    def test_to_dict(self):
        """Test the to_dict() function"""
        model = BaseModel()
        model.name = "Betty"
        model.age = 100
        dict = model.to_dict()
        self.assertEqual(dict["__class__"], "BaseModel")
        self.assertEqual(dict["name"], "Betty")
        self.assertEqual(dict["age"], 100)
        self.assertEqual(dict["created_at"], model.created_at.isoformat())
        self.assertEqual(dict["updated_at"], model.updated_at.isoformat())

    def test_instantiation_kwargs(self):
        """Test instantiation with kwargs"""
        model = BaseModel()
        model.name = "Betty"
        model.age = 100
        model_json = model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertIs(type(new_model), BaseModel)
        self.assertIs(type(new_model.id), str)
        self.assertEqual(new_model.id, model.id)
        self.assertIs(type(new_model.created_at), datetime)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertIs(type(new_model.updated_at), datetime)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertIs(type(new_model.name), str)
        self.assertEqual(new_model.name, "Betty")
        self.assertIs(type(new_model.age), int)
        self.assertEqual(new_model.age, 100)

    def test_str(self):
        """test the output of the instance when printed"""
        a = BaseModel()
        self.assertEqual(str(a), f"[{a.__class__.__name__}] ({a.id}) " +
                         f"{a.__dict__}")

    


if __name__ == '__main__':
    unittest.main()
