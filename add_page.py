import os
import re

### Global configuration

# template for index page
index_template = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <!-- Zero MD to view markdown -->
    <script type="module" src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@2/dist/zero-md.min.js"></script>

    <title>Byte Sized Code - Learn C!</title>
  </head>
  <body class="bg-light">
    <div class="bg-dark text-info p-3 container-fluid d-flex">
      <div class="col-2 text-center">
        <a class="btn btn-secondary" href="index.html">
          Home
        </a>
      </div>
      <h3 class="text-center col-8">
        <b>Learn C</b>
      </h3>
      <div class="dropdown col-2 text-center">
        <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
          Posts
        </a>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
          {}
        </ul>
      </div>
    </div>

    <div class="container-fluid text-center p-3 py-5">
      <div class="row">
        <div class="col"></div>
        <div class="col-6">
          <p>
            This website is dedicated to helping people learn about C for free.
            It is recommended to go through the articles according to the order in which they are presented.
          </p>
          <a class="btn btn-secondary" style="font-size: 30px;border-radius:10px;" href="0. Keywords and Identifiers.html">Go to First Lesson</a>
          <hr>
          <p>
            However, if you feel confident about a topic, you can skip the article and jump to any article by using the dropdown menu in the top right corner.
          </p>
          <p>
            If you like the work and would like to support such endeavours:
          </p>
          <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="aceking007" data-color="#5F7FFF" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#ffffff" data-coffee-color="#FFDD00" ></script>
        </div>
        <div class="col"></div>
      </div>
    </div>

    <footer class="footer mt-auto p-3 text-center">
      <span class="text-muted">&#169; Arpit Omprakash (<a href="https://github.com/aceking007">aceking007</a>)</span>
    </footer>

    <!-- Bootstrap JavaScript -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>

  </body>
</html>"""

# template for webpage
template = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <!-- Zero MD to view markdown -->
    <script type="module" src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@2/dist/zero-md.min.js"></script>

    <title>{}</title>
  </head>
  <body class="bg-light text-white">
    <div class="bg-dark text-info p-3 container-fluid d-flex">
      <div class="col-1">
        <a class="btn btn-secondary" href="index.html">
          Home
        </a>
      </div>
      <h3 class="text-center col-10">
        <b>Learn C</b>
      </h3>
      <div class="dropdown col-1">
        <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
          Posts
        </a>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
          {}
        </ul>
      </div>
    </div>

    <div class="container-fluid p-5">
    <zero-md src="{}" crossorigin="anonymous"></zero-md>
    </div>

    <div class="bg-light text-center p-2">
      <a href="{}">
        prev
      </a>
      |
      <a href="{}">
        next
      </a>
    </div>

    <footer class="footer mt-auto p-3 text-center">
        <span class="text-muted">&#169; Arpit Omprakash (<a href="https://github.com/aceking007">aceking007</a>)</span>
    </footer>


    <!-- Bootstrap JavaScript -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>

  </body>
</html>"""

# prepend to convert link to raw url
prepend = r"https://raw.githubusercontent.com/Byte-Sized-Code/LearnC/main/"

### Variables

# list of pages already built
built_pages = []

# list of pages to build
to_build = []

# html for dropdownmenu
dropdown_html = ""

# populating the list of pages built
with open(r"pages_built.log", "r") as file:
    for line in file:
        built_pages.append(line.strip())

print("Pages already built")
print(built_pages)


# find all the files with .md extension not in list of built pages
for root, dirs, files in os.walk(r"C:\Users\ARPIT\Documents\GitHub\LearnC"):
    for file in files:
        if file.endswith(".md"):
            if file not in built_pages:
                print("Reading File")
                print(file)
                # add path of file and filename to the build list
                f = os.path.join(root, file)
                fname = os.path.splitext(file)[0]
                to_build.append([f, fname])

# add posts to dropdown menu
for page in to_build:
    filename = "{}.html".format(page[1])
    name = page[1][3:]
    dropdown_html += "<li><a class='dropdown-item' href='{}'>{}</a></li>".format(filename, name)

# build the index page
print("Building index page")
with open(r"docs\index.html", "w") as fd:
    fd.write(index_template.format(dropdown_html))

# build pages
for i in range(len(to_build)):
    if i != 0:
        prev = "{}.html".format(to_build[i-1][1])
    else:
        prev = "#"
    page = to_build[i]
    if i == len(to_build) - 1:
        next = "#"
    else:
        next = "{}.html".format(to_build[i+1][1])
    # address for the raw md file after upload
    addr = re.sub(' ', '%20', page[0]).replace('\\', '/')
    address = prepend + re.search('LearnC/(.*)', addr)[1]
    # write the html file in doc directory
    title = "Learn C - " + page[1][3:]
    filename = r"docs\{}.html".format(page[1])
    print("Building Page")
    print(filename)
    with open(filename, "w") as file:
        file.write(template.format(title, dropdown_html, address, prev, next))
