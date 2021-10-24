import os

files = ['p5.js', 'p5.sound.min.js', 'math.js', 'p5.strive.js', 'skulpt.min.js', 'skulpt-stdlib.js', 'jquery-3.5.1.min.js', 'skulptSetup.js']

package = ''

for fn in files:
  path = os.path.join(os.getcwd(), 'editor', fn)
  with open(path) as f:
    for line in f:
      package += line
  package += '\n'

with open('strive.js', 'w') as f:
  f.write(package)
