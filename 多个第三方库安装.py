import os
libs = {"numpy","matplotlib","pillow"}
try:
    for lib in libs:
        os.system("pip install "+lib)
        print("successful")
except:
    print("Failed Somehow")