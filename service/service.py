import os

to_exec=os.environ.get('EXEC', '''
for k in os.environ:
  print("%s: %s" % (k, os.environ[k]))
''')
exec(to_exec)
