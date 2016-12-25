import re, os.path, sys, requests, urllib

regexp = re.compile("((http://[^)]+))")
regexp1 = re.compile("(\[[^]]+\])")
r = requests.get("https://gist.githubusercontent.com/bishboria/8326b17bbd652f34566a/raw/0594f99c580c3befb924f3d36ab187c2da8f441b/springer-free-maths-books.md")
htmlList = map(lambda x: x.strip(), r.content.split("\n\n"))
for line in htmlList:
    match = regexp.search(line)
    if match:
        counter = 0
        url = match.groups()[0]
        origname = re.sub("[?.:*\[\]\"]", "", regexp1.search(line).groups()[0]).replace(",", " -") + ".pdf"
        fname = origname
        while os.path.isfile(fname):
            counter += 1
            if counter != 0:
                fname = origname.replace(".pdf", " " + str(counter) + ".pdf")
        sys.stdout.write("Downloading html line " + str(htmlList.index(line)) + " " + url + " as " + fname + "...\n")
        urllib.urlretrieve(url, fname)