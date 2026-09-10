import importlib, json, os, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src/chromalearn'))
class StorageTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();base=Path(self.t.name);os.environ['CHROMALEARN_CONFIG']=str(base/'etc/config.json');os.environ['CHROMALEARN_PROFILE_DIR']=str(base/'profiles')
  import storage;self.s=importlib.reload(storage)
 def tearDown(self): self.t.cleanup()
 def test_default_config(self): self.assertEqual(self.s.load_config()['model'],'local-model')
 def test_save_config_strips_secret(self):
  c=self.s.load_config();c['api_key']='secret';self.s.save_config(c);self.assertNotIn('api_key',json.loads(self.s.SYSTEM_CONFIG.read_text()))
 def test_profile_roundtrip(self):
  p=self.s.save_profile({'id':'math7','name':'Math','help_level':4});self.assertEqual(self.s.get_profile('math7')['help_level'],4)
 def test_bad_id(self):
  with self.assertRaises(ValueError): self.s.save_profile({'id':'../../bad'})
 def test_bad_mode(self):
  with self.assertRaises(ValueError): self.s.save_profile({'id':'x','assessment_mode':'cheat'})
 def test_delete_default_denied(self):
  with self.assertRaises(ValueError): self.s.delete_profile('default')
 def test_no_adaptive_persistence_api_in_storage(self):
  self.assertFalse(hasattr(self.s,'save_adaptive_data'));self.assertFalse(hasattr(self.s,'load_adaptive_data'));self.assertFalse(hasattr(self.s,'adaptive_file'))
if __name__=='__main__':unittest.main()
