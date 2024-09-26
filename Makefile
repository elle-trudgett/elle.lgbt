# Find all Markdown files in the content-root directory
MD_FILES := $(wildcard content-root/*.md)

# Create a list of target HTML files in the deploy folder
HTML_FILES := $(patsubst content-root/%.md,deploy/%.html,$(MD_FILES))

# Default target
all: $(HTML_FILES)
	python assemble.py

# Rule to build HTML files from Markdown
deploy/%.html: content-root/%.md deploy/index.css template.html Makefile
	mkdir -p deploy
	pandoc --toc -s --css reset.css --css index.css -i $< -o $@ --template=template.html

# Clean target
clean:
	rm -f $(HTML_FILES)

.PHONY: all clean
