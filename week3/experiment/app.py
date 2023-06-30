from jinja2 import Template

templ = """hello {{name}}"""

TEMPLATE = """
this is {p:+} and this is {n:+} 

this is in decimal = {value:d} and in hex={value:x}
"""
# prints the sign of the number 
# prints value and hexcode 

data = [
        {'year' : 2000, 'address' : 'kolkata ,india', 'language' : 'english'},
        {'year' : 2001, 'address' : 'delhi ,india', 'language' : 'hindi'},
        {'year' : 2002, 'address' : 'blr ,india', 'language' : 'python'},
        {'year' : 2004, 'address' : 'chennai ,india', 'language' : 'bengali'},
    ]

def main() : 
    print(TEMPLATE.format(p = 5, n= -0.7, value = 11))

    # for jinja 
    temp = Template(templ)
    print(temp.render(name = 'ghorai'))

    # pass in the data in the template 
    html_template = open('base.html.jinja2', 'r')
    html_template_content = html_template.read()
    html_template.close()

    html_temp = Template(html_template_content)
    content = html_temp.render(data = data)
    
    html_doc = open('index.html', 'w')
    html_doc.write(content)
    html_doc.close()


if __name__ == "__main__" : 
    # execute only if run as script 
    main()