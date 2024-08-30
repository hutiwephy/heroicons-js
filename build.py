import sys, os, glob, json

tree = {}

for dir in glob.glob(os.path.join(os.path.dirname(sys.argv[:1][0]), "heroicons/optimized/24/*/")):
    key0 = os.path.basename(dir.removesuffix("\\").removesuffix("/"))
    print(f"[{key0}]: {dir}")
    tree[key0] = {}
    for file in glob.glob(os.path.join(dir, "*.*")):
        key1 = os.path.basename(file.removesuffix("\\").removesuffix("/")).split(".")[0]
        print(f"  [{key1}]: {file}")

        tmp = open(file, "r")
        tree[key0][key1] = tmp.read()
        tmp.close()

tmp = open(os.path.join(os.path.dirname(sys.argv[:1][0]), "heroicons.js"), "r")
script = tmp.read()
tmp.close()
script = script.replace("$ICONDB", json.dumps(tree, indent=4))
tmp = open(os.path.join(os.path.dirname(sys.argv[:1][0]), "heroicons.css"), "r")
script = script.replace("$ICONCSS", tmp.read().replace("\n", "").replace("    ", "").replace("\t", ""))
tmp.close()


if(not os.path.exists("build")):
    os.makedirs("build")
tmp = open(os.path.join(os.path.dirname(sys.argv[:1][0]), "build/heroicons.js"), "w")
tmp.write(script)
tmp.close()
