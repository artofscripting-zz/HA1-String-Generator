import hashlib
import time
m = hashlib.md5()
if len(sys.argv) > 3:
	ha1String = sys.argv[1] + sys.argv[2] + sys.argv[3]
	m.update(ha1String)
	print (m.hexdigest())
else:
    needArg = 'EXAMPLE "py.exe HA1_String_Generator.py username realm password"'
    print (needArg)
    time.sleep(60)
