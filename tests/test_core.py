import unittest
from sqlite_constraint_replay import run
class Tests(unittest.TestCase):
 def ops(self):return [{'op':'insert','table':'child','id':1,'parent_id':7},{'op':'insert','table':'parent','id':7}]
 def test_deferred_child_before_parent_commits(self):
  r=run({'deferred':True,'operations':self.ops()});self.assertTrue(r['committed']);self.assertEqual(r['child_rows'],[[1,7]]);self.assertEqual(r['foreign_key_violations'],[])
 def test_immediate_failure_rolls_back_transaction(self):
  r=run({'operations':self.ops()});self.assertFalse(r['committed']);self.assertEqual(r['error']['stage'],'operation');self.assertEqual(r['child_rows'],[]);self.assertEqual(r['parent_rows'],[])
 def test_commit_failure_is_distinct(self):
  r=run({'deferred':True,'operations':self.ops()[:1]});self.assertEqual(r['error']['stage'],'commit');self.assertEqual(r['child_rows'],[])
 def test_disabled_enforcement_still_reports_orphans(self):
  r=run({'foreign_keys':False,'operations':self.ops()[:1]});self.assertTrue(r['committed']);self.assertEqual(len(r['foreign_key_violations']),1)
 def test_null_reference_is_permitted_by_native_sqlite(self):
  r=run({'operations':[{'op':'insert','table':'child','id':2,'parent_id':None}]});self.assertTrue(r['committed']);self.assertEqual(r['child_rows'],[[2,None]])
