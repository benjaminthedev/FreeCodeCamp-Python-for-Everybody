# What will the output of the following code be like?:

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# Answer

# Just contents of "romeo.txt".
