# https://github.com/jupyter/nbconvert/issues/699
import nbformat
import nbconvert
import sys

if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], 'filename.ipynb', '[--slides]')
    exit(-1)

with open(sys.argv[1]) as nb_file:
    nb_contents = nb_file.read()

# Convert using the ordinary exporter
notebook = nbformat.reads(nb_contents, as_version=4)
if len(sys.argv) == 3 and sys.argv[2] == '--slides':
    outname = sys.argv[1].split('.ipynb')[0] + '.slides.html'
    print("Converting to slides:", outname)    
    exporter = nbconvert.SlidesExporter()    
else:
    outname = sys.argv[1].split('.ipynb')[0] + '.html'
    print("Converting to HTML:", outname)
    exporter = nbconvert.HTMLExporter()
    
body, res = exporter.from_notebook_node(notebook)

# Create a list saving all image attachments to their base64 representations
images = []
for cell in notebook['cells']:
    if 'attachments' in cell:
        attachments = cell['attachments']
        for filename, attachment in attachments.items():
            for mime, base64 in attachment.items():
                images.append( [f'attachment:{filename}', f'data:{mime};base64,{base64}'] )

# Fix up the HTML and write it to disk
for itmes in images:
    src = itmes[0]
    base64 = itmes[1]
    body = body.replace(f'src="{src}"', f'src="{base64}"', 1)
    
with open(outname, 'w') as output_file:
    output_file.write(body)