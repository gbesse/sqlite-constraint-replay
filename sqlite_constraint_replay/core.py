import sqlite3
from .common import integer

def run(data):
 deferred=data.get('deferred',False);enabled=data.get('foreign_keys',True)
 if type(deferred)is not bool or type(enabled)is not bool:raise ValueError('boolean')
 operations=data['operations']
 if len(operations)>500:raise ValueError('operations')
 for r in operations:
  if r['table']not in ('parent','child')or r['op']not in ('insert','delete'):raise ValueError('operation')
  integer(r['id'],-1000000,1000000)
  if r['table']=='child'and r['op']=='insert'and r.get('parent_id')is not None:integer(r['parent_id'],-1000000,1000000)
 c=sqlite3.connect(':memory:');trace=[];error=None;stage='operation'
 try:
  c.execute('PRAGMA foreign_keys='+('ON'if enabled else'OFF'));c.execute('CREATE TABLE parent(id INTEGER PRIMARY KEY)');c.execute('CREATE TABLE child(id INTEGER PRIMARY KEY,parent_id INTEGER REFERENCES parent(id) '+('DEFERRABLE INITIALLY DEFERRED'if deferred else'NOT DEFERRABLE')+')');c.commit();c.execute('BEGIN')
  try:
   for i,r in enumerate(operations):
    if r['op']=='delete':c.execute('DELETE FROM '+r['table']+' WHERE id=?',(r['id'],))
    elif r['table']=='parent':c.execute('INSERT INTO parent VALUES (?)',(r['id'],))
    else:c.execute('INSERT INTO child VALUES (?,?)',(r['id'],r.get('parent_id')))
    trace.append({'operation':i,'accepted_before_commit':True})
   stage='commit';c.commit();committed=True
  except sqlite3.IntegrityError as exc:
   error={'stage':stage,'operation':len(trace)if stage=='operation'else None,'sqlite_code':exc.sqlite_errorname};c.rollback();committed=False
  return {'committed':committed,'error':error,'trace':trace,'parent_rows':[list(r)for r in c.execute('SELECT * FROM parent ORDER BY id')],'child_rows':[list(r)for r in c.execute('SELECT * FROM child ORDER BY id')],'foreign_key_violations':[list(r)for r in c.execute('PRAGMA foreign_key_check')],'foreign_keys_enabled':bool(c.execute('PRAGMA foreign_keys').fetchone()[0]),'deferred':deferred,'sqlite_version':sqlite3.sqlite_version}
 finally:c.close()
