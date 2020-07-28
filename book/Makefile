
CHAPTERS := Header.yml \
before_you_begin.md \
appendix_conda_and_pymol.md \
writing_a_program.md \
dealing_with_values.md \
the_order_of_events.md \
controlling_execution.md \
organizing_your_code.md \
python_values_are_objects.md \
structuring_data.md \
glueing_values_in_sequence.md \
iteration_over_values.md \
testing_your_code.md \
working_with_files.md \
translation_project.md \
hiv_project.md \
codonbias_project.md \
alignment_project.md \
seqdist_project.md \
assembly_project.md \
orf_project.md \
general_exercises.md \
unleash_your_functions.md \
building_lists_on_the_fly.md \
your_own_types_of_objects.md \
python_modules.md \
biopython.md \
references.md
SOURCE_CHAPTERS := $(foreach chapter,$(CHAPTERS),chapters/$(chapter))

PYMOL_INST := chapters/pymol.md


PANDOC := pandoc

PANDOC_OPTS_ALL :=  --toc \
                    -f markdown-smart \
					--top-level-division=chapter \
					--variable urlcolor=cyan \
					--filter pandoc-crossref \
					--filter pandoc-citeproc \
					--number-sections \
					--toc-depth=2 \
					--highlight-style=kate

# PANDOC_OPTS_ALL :=  -S --toc --smart \
# 					--top-level-division=chapter \
# 					--filter pandoc-crossref \
# 					--filter pandoc-citeproc \
# 					--listings -H listings-setup.tex 


PANDOC_PDF_OPTS := $(PANDOC_OPTS_ALL) \
					--default-image-extension=pdf \
					--variable documentclass=scrbook \
					--template=latex_template.tex \
					--variable=geometry:a4paper
#    				--variable=fontfamily:arev
					# --variable links-as-notes \


PANDOC_EPUB_OPTS := $(PANDOC_OPTS_ALL) \
					--default-image-extension=png \
					-t epub3 --toc-depth=1 \
					--epub-cover-image=cover.png

book.pdf: $(SOURCE_CHAPTERS) Makefile latex_template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(SOURCE_CHAPTERS)

book.epub: $(SOURCE_CHAPTERS) Makefile
	$(PANDOC) $(PANDOC_EPUB_OPTS) -o $@ $(SOURCE_CHAPTERS)

book.mobi: book.epub
	./kindlegen book.epub -o book.mobi


extra_material.pdf: $(EXTRA_CHAPTERS) Makefile latex_template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(EXTRA_CHAPTERS)

general_exercises.pdf: $(GENERAL_EXERCISES) Makefile latex_template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(GENERAL_EXERCISES)

pymol.pdf: $(PYMOL_INST) Makefile latex_template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(PYMOL_INST)



book: book.pdf book.epub book.mobi

pymol: pymol.pdf

all: book.pdf book.epub book.mobi pymol.pdf

clean:
	rm book.pdf book.epub book.mobi pymol.pdf
