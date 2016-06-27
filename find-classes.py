# Find classes in a css file and an html file and compare the results

import re

pattern = re.compile("(?<![a-zA-Z0-9])(\.[a-zA-Z0-9_-]+)(?=[ ,\{])") 
# need to see if we can get rid of 0.77 type things...

pattern_html = re.compile("class=\"([a-zA-Z0-9\_\-\ ]+)\"") 
pattern_html_classes = re.compile("([a-zA-Z0-9\_\-]+)") 

styles, html, extras = [], [], []

# Search style file and create a list
print("\n\nSearching styles file\n")

for i, line in enumerate(open('screen.css')):
    for match in re.finditer(pattern, line):
        # print ('Found on line %s: %s' % (i+1, match.group(0)))
        # print(match.group(0))
        if match.group(0) not in styles:
            if match.group(0)[:1] == ".":
                styles.append(match.group(0)[1:])

print("\nStyles Output:\n")
print(styles)

# Search HTML file and create a list
print("\nSearching HTML file\n")

for i, line in enumerate(open('index.html')):
    for match in re.finditer(pattern_html, line):
        result = match.group(0)
        results = []

        # print ('Found on line %s: %s' % (i+1, result))

        m = re.findall('([a-zA-Z0-9\_\-]+\s?)', str(result))
        if m:
            for classes in m:
                if classes.strip() not in html:
                    html.append(classes.strip())
            # print("submatch results: " + str(m))

        # # print(match.group(0))
        # if match.group(0) not in html:
        #     html.append(match.group(0))

print("\nHTML Output:\n")
print(html)

# Compare the lists and output extras (in css but not html) to a third list
print("comparing")

for list_item in styles:
    if list_item not in html:
        print("not found: " + list_item)
        if list_item not in extras:
            extras.append(list_item)

print("here's your extra stuff:")
print(extras)

# Output the results to a file
output_file = "data/outputs.txt"
with open(output_file, "w") as file_object:
    file_object.write("Styles results:\n\n")
    file_object.write(str(styles))
    file_object.write("\n\n------\n\n")
    file_object.write("HTML results:\n\n")
    file_object.write(str(html))
    file_object.write("\n\n------\n\n")
    file_object.write("Extras results (items in the STYLES file that are NOT in the HTML file):\n\n")
    file_object.write(str(extras))
    file_object.write("\n\n------\n\n")
