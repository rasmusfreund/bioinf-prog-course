## Notes for chapter 8 {-}

### Part I: DNA Sequence Traces and Base-Calling

1. Access the Trace Archive database: As described in the book. However, if you do the direct search in Google, you might end up somewhere else. To make sure that you are on the right web site, go to https://trace.ncbi.nlm.nih.gov/Traces/trace.cgi .
2.  Visualize the Trace of a sequence and base calling problems: As described in the book. A tip: when you search for Ns, you can first find one in the FASTA sequence and then try to find it in the Trace.


### Part II: Metagenomic Analysis of the Human Virome by Next-Generation Sequencing

1. Downloading data from EBI / NCBI: Once you are in Galaxy, the book tells you to download FASTQ files through the EBI tool. This doesn’t work. The way to get the data the book is working on is: 
    -     On the Tools menu, search for the submenu NCBI SRA Tools
    -     Click on the Download and Extract Reads in FASTA/Q format from NCBI SRA
    -     In the Accession box, copy one of the following accession numbers:

        SRR057872, SRR057873, SRR057881, SRR057883, SRR057884, SRR057887, SRR057888, SRR057889, SRR057890, SRR057893, SRR057894, SRR057895

It is fine that different students take different accession numbers. This way, you are going to get different results that will be complementary to each other.

    -    Click on Execute.
    -    Now, you can follow the book instructions from the point it tells you to run the tool FASTQ Groomer. 

2. Transform and process the FASTQ file downloaded: As described in the book from the FASTQ Groomer to the Tabular-to-FASTA.

3. Megablast and taxonomic analysis: The tool the book tells you to use not only requires you to register in Galaxy to be used but also it does not work. Therefore, we are going to do a similar procedure using BLAST to get similar conclusions (recall chapter 4 web exercises for it):

    -    Download the FASTA file you generated in the step Tabular-to-FASTA. To do that, you can click on the box corresponding to that procedure on the history panel and click on the floppy disk symbol.
    -    Go to BLAST in NCBI (https://blast.ncbi.nlm.nih.gov/Blast.cgi).
    -    Select “Nucleotide BLAST”
    -    Open the FASTA file you’ve just downloaded from Galaxy with a text editor (sublime will work) and copy a bunch of sequences (around 100).
    -    Paste those sequences in the white input box on the BLAST page and submit the job pressing the button “BLAST” at the end of the page.
    -    Once the BLAST is done, you will have the result page that looks like figure 4.6 from chapter 4 (page 72).

In the name of the sequences that best align with your query (in the (B) part in figure 4.6) will tell you which species the sequence you inputted is most similar to. 

To check another query sequence, go back to the top of the result page and select another query in the drop-down menu next to “Results for: ” (in the (A) part in figure 4.6).

    -    Write down the species you find to be part of your sample for different queries.  


NOTE: You will not be able to answer the web exercises completely. However, try to answer them with the results you got. 


### Part III: Assembling the Sequence of a Novel Virus

1. Assembling the virus sequence: As described in the book. The FASTA sequence that they call reads.txt is saved in the Dropbox folder as:

CH08Simulated454sequencingreadsfromanunknownvirusgenome.txt

2. Extra analysis to answer the web exercise questions: Go to Clustal Omega web service in EMBL-EBI web page ([https://www.ebi.ac.uk/Tools/msa/clustalo/]()) which is a multiple sequence aligner. Change the “Protein” in the “Step 1 - Enter your input sequence” for “DNA”. Copy and paste the contigs you’ve produced after running the assembler and the Klassevirus reference genome sequence in the Exercise 8 Dropbox folder CH08Klassevirusgenome.txt. Then, submit the job. Doing that, you will easily compare the contigs with the reference genome and get conclusions to answer different web exercise questions of this part III.





