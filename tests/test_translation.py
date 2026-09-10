import json, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src/chromalearn'))
import translation

class TranslationTests(unittest.TestCase):
    def test_rejects_runtime_profile_path(self):
        with self.assertRaises(ValueError):
            translation._check_input(Path('/var/lib/chromalearn/profiles/test.json'))

    def test_json_key_shape_detects_changed_keys(self):
        a={'title':'Hej','nested':{'x':'Y'}}
        b={'title':'Hello','nested':{'x':'Y'}}
        c={'title':'Hello','nested':{'z':'Y'}}
        self.assertEqual(translation._key_shape(a), translation._key_shape(b))
        self.assertNotEqual(translation._key_shape(a), translation._key_shape(c))

    def test_markdown_draft_banner_and_output(self):
        old=translation._translate_markdown
        translation._translate_markdown=lambda config,text,language:'# Translated\n'+text
        try:
            with tempfile.TemporaryDirectory() as td:
                src=Path(td)/'x.md'; src.write_text('# Hej\n',encoding='utf-8')
                out=Path(td)/'out.md'
                dest,review=translation.translate_file(src,'English','en',out,config={})
                self.assertTrue(dest.exists()); self.assertTrue(review.exists())
                self.assertIn(translation.DRAFT_BANNER,dest.read_text())
        finally:
            translation._translate_markdown=old

    def test_json_translation_structure_guard(self):
        old=translation.call_model
        translation.call_model=lambda config,messages:'{"title":"Hello","nested":{"x":"Value"}}'
        try:
            result=translation._translate_json({},'{"title":"Hej","nested":{"x":"Værdi"}}','English')
            self.assertEqual(json.loads(result)['title'],'Hello')
        finally:
            translation.call_model=old

if __name__=='__main__': unittest.main()
