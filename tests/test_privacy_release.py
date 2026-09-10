import subprocess, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class PrivacyRelease(unittest.TestCase):
 def test_canary_scanner_clean_and_detects(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d); marker='CHROMALEARN-CANARY-UNIT-91827'
   r=subprocess.run(['python3',str(ROOT/'packaging/chromalearn-privacy-scan'),marker,str(d)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0);self.assertIn('No canary found',r.stdout)
   (d/'leak.txt').write_text('prefix '+marker+' suffix')
   r=subprocess.run(['python3',str(ROOT/'packaging/chromalearn-privacy-scan'),marker,str(d)],capture_output=True,text=True)
   self.assertEqual(r.returncode,1);self.assertIn('leak.txt',r.stdout)
 def test_docs_state_current_upgrade_boundary(self):
  readme=(ROOT/'README.md').read_text()
  ops=(ROOT/'docs/PRIVACY_OPERATIONS.md').read_text()
  self.assertIn('udfører ingen automatisk oprydning',readme)
  self.assertIn('indeholder ingen automatisk migration eller sletterutine',ops)
 def test_source_has_no_adaptive_writer(self):
  for p in (ROOT/'src/chromalearn').glob('*.py'):
   txt=p.read_text();self.assertNotIn('save_adaptive_data',txt)
 def test_packaging_contains_only_current_privacy_tools(self):
  names={p.name for p in (ROOT/'packaging').iterdir() if p.is_file()}
  self.assertEqual(names,{'chromalearn-privacy-scan','chromalearn-translate','chromalearn.desktop','chromalearn.svg'})
 def test_pytest_cache_is_ignored_and_excluded(self):
  ignore=(ROOT/'.gitignore').read_text()
  self.assertIn('.pytest_cache/',ignore)
  build=(ROOT/'build_deb.sh').read_text()
  self.assertIn("--exclude='./.pytest_cache'",build)
if __name__=='__main__':unittest.main()
