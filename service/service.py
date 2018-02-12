import os
import json

env=os.environ.get('EXEC', '["for k in os.environ:","  print(\\"%s: %s\\" % (k, os.environ[k]))"]')
cmd=json.loads(env)
if isinstance(cmd, list):
 cmd="\n".join(cmd)

exec(cmd)
