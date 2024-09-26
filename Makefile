
# Find all Markdown files in the current directory
MD_FILES := $(wildcard *.md)

# Create a list of target HTML files
HTML_FILES := $(MD_FILES:.md=.html)

# Default target
all: $(HTML_FILES)
	python assemble.py

# Rule to build HTML files from Markdown
%.html: %.md index.css template.html Makefile
	pandoc --toc -s --css reset.css --css index.css -i $< -o $@ --template=template.html

# Clean target
clean:
	rm -f $(HTML_FILES)

.PHONY: all clean
