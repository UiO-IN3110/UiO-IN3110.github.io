import glob
import os
import re

REGEX = r"""\\begin\{document\}((?:.|\n)*?)\\end\{document\}"""

os.chdir("py")
globs = glob.glob("*.py")
os.chdir(os.pardir)

if os.path.isfile("slides.tex"):
    os.remove("slides.tex")

for filename in globs:
    filename = filename[:-3]
    print("copying %s..." % filename)
    os.system(f"pygmentize -f latex -O full py/{filename}.py > tex/{filename}.tex")

    with open("tex/%s.tex" % filename) as src:
        text = src.read()

    text = re.findall(REGEX, text, flags=re.M)[0]
    with open("tex/%s.tex" % filename, "w") as dst:
        dst.write(text)

    with open("slides.tex", "a") as dst:
        dst.write(
            """
\\begin{frame}[shrink=20]
  \\input{tex/%s}
\\end{frame}"""
            % filename
        )
