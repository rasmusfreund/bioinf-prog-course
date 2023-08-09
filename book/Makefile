
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
1.md \
preface.md \
python/before_you_begin.md \
python/appendix_conda_and_pymol.md \
python/writing_a_program.md \
python/dealing_with_values.md \
2.md \
python/the_order_of_events.md \
python/do_the_steps.md \
bioinf/bioinf_resources.md \
python/controlling_behavior.md \
3.md \
python/organizing_your_code.md \
python/testing_your_code.md \
bioinf/gwas.md \
python/python_values_are_objects.md \
4.md \
python/iteration_over_values.md \
bioinf/assembly_and_mapping.md \
python/working_with_data_files.md \
project/some_new_project_without_iteration.md \
5.md \
python/lists.md \
bioinf/procaryote_gene_fiding.md \
project/folding_project.md \
6.md \
python/gluing_values_in_sequence.md \
python/using_code_from_other_files.md \
python/on_the_shoulders_of_giants.md \
project/orf_project.md \
7.md \
python/dictionaries.md \
bioinf/pairwise_alignment.md \
python/your_own_types_of_objects.md \
project/translation_project.md \
8.md \
bioinf/protein_substitution_matrices.md \
bioinf/database_searching.md \
project/alignment_project.md \
9.md \
python/unleash_your_functions.md \
bioinf/multiple_alignment.md \
bioinf/models_of_dna_evolution.md \
project/hiv_project.md \
10.md \
bioinf/clustering.md \
bioinf/phylogenetics.md \
project/seqdist_project.md \
11.md \
bioinf/hidden_markov_models.md \
bioinf/neural_networks.md \
12.md \
bioinf/sequence_annnotation.md \
13.md \
project/assembly_project.md \
14.md \
bioinf/rna_structure.md \
references.md



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

master_in_bioinformatics.pdf: chapters/master_in_bioinformatics.md Makefile header_extra.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) -o $@ chapters/master_in_bioinformatics.md

master: master_in_bioinformatics.pdf

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
