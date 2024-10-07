# Find all Markdown files in the content-root directory and its subdirectories
MD_FILES := $(shell find content-root -name '*.md')

# Create a list of target HTML files in the deploy folder
HTML_FILES := $(patsubst content-root/%.md,deploy/%.html,$(MD_FILES))

# Default target
all: pre-assemble $(HTML_FILES)
	python assemble.py

pre-assemble:
	python preassemble.py

# Rule to build HTML files from Markdown
deploy/%.html: content-root/%.md deploy/index.css template.html Makefile
	@mkdir -p $(@D)
	pandoc --toc -s --css '/reset.css' --css '/index.css' -i $< -o $@ --template=template.html

# Clean target
clean:
	rm -rf deploy

.PHONY: all clean pre-assemble