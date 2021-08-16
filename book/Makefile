
PANDOC := pandoc

PANDOC_OPTS_ALL :=  --toc \
                    -f markdown-smart \
					--top-level-division=chapter \
					--variable urlcolor=cyan \
					--filter pandoc-crossref \
					--citeproc \
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
					--include-in-header=header_extra.tex \
					--variable=geometry:a4paper
#					--template=latex_template.tex \
#    				--variable=fontfamily:arev
					# --variable links-as-notes \


PANDOC_EPUB_OPTS := $(PANDOC_OPTS_ALL) \
					--default-image-extension=png \
					-t epub3 --toc-depth=1 \
					--epub-cover-image=cover.png

# Programming notes
CHAPTERS := Header.yml \
00_preface.md \
01_before_you_begin.md \
02_appendix_conda_and_pymol.md \
03_writing_a_program.md \
04_dealing_with_values.md \
05_the_order_of_events.md \
06_controlling_behavior.md \
07_organizing_your_code.md \
08_python_values_are_objects.md \
09_structuring_data.md \
10_gluing_values_in_sequence.md \
11_iteration_over_values.md \
12_testing_your_code.md \
13_working_with_files.md \
14_your_own_types_of_objects.md \
translation_project.md \
assembly_project.md \
alignment_project.md \
codonbias_project.md \
hiv_project.md \
seqdist_project.md \
orf_project.md \
folding_project.md \
references.md

# pairwise_alignment.md \
# models_of_dna_evolution.md \
# protein_substitution_matrices.md \
# clustering.md \
# unleash_your_functions.md \
# phylogenetics.md \
# hidden_markov_models.md \

SOURCE_CHAPTERS := $(foreach chapter,$(CHAPTERS),chapters/$(chapter))

book.pdf: $(SOURCE_CHAPTERS) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(SOURCE_CHAPTERS)

book.epub: $(SOURCE_CHAPTERS) Makefile
	$(PANDOC) $(PANDOC_EPUB_OPTS) -o $@ $(SOURCE_CHAPTERS)

book.mobi: book.epub
	./kindlegen book.epub -o book.mobi

book: book.pdf book.epub book.mobi


# PyMol installation howto
pymol.pdf: chapters/pymol.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/pymol.md

pymol: pymol.pdf

# Individually compiled programming projects
translation_project.pdf: chapters/translation_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/translation_project.md

assembly_project.pdf: chapters/assembly_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/assembly_project.md

alignment_project.pdf: chapters/alignment_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/alignment_project.md

hiv_project.pdf: chapters/hiv_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/hiv_project.md

seqdist_project.pdf: chapters/seqdist_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/seqdist_project.md

orf_project.pdf: chapters/orf_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/orf_project.md

folding_project.pdf: chapters/folding_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/folding_project.md
	
codonbias_project.pdf: chapters/codonbias_project.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/codonbias_project.md

PROJECT_PDFS := translation_project.pdf assembly_project.pdf alignment_project.pdf hiv_project.pdf \
	seqdist_project.pdf orf_project.pdf folding_project.pdf codonbias_project.pdf

projects: $(PROJECT_PDFS)





extra_material.pdf: $(EXTRA_CHAPTERS) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(EXTRA_CHAPTERS)

general_exercises.pdf: $(GENERAL_EXERCISES) Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ $(GENERAL_EXERCISES)





all: book.pdf book.epub book.mobi pymol.pdf $(PROJECT_PDFS)

clean:
	rm book.pdf book.epub book.mobi pymol.pdf $(PROJECT_PDFS)
