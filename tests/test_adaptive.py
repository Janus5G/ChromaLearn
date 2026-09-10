import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src/chromalearn'))
from adaptive import AdaptiveProfile

class Adaptive(unittest.TestCase):
 def test_subject_topic_profiles_are_independent_in_memory(self):
  a=AdaptiveProfile('Matematik','ligninger');b=AdaptiveProfile('Engelsk','udtale')
  a.record('visual',2);a.record('text',0);b.record('audio',2);b.record('text',0)
  self.assertEqual(a.recommendation()['modality'],'visual')
  self.assertEqual(b.recommendation()['modality'],'audio')
 def test_evidence_changes_ranking(self):
  a=AdaptiveProfile('Fysik','kraft');a.record('text',0);a.record('activity',2);a.record('text',1);a.record('activity',2)
  self.assertEqual(a.recommendation()['modality'],'activity');self.assertAlmostEqual(a.public_summary()['activity']['score'],1.0)
 def test_invalid_scores_fail(self):
  a=AdaptiveProfile('x')
  with self.assertRaises(ValueError): a.record('text',3)
  with self.assertRaises(ValueError): a.record('video',1)
 def test_new_session_has_no_previous_evidence(self):
  a=AdaptiveProfile('Matematik','brøker');a.record('visual',2)
  b=AdaptiveProfile('Matematik','brøker')
  self.assertEqual(b.public_summary()['visual']['attempts'],0)
  self.assertIsNone(b.public_summary()['visual']['score'])
if __name__=='__main__':unittest.main()
