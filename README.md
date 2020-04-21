# SciBert
Creation of word embedding using SciBert

# These are the steps to follow
1. Install the packeges
    pip3 install -U bert-serving-server bert-serving-client
    pip3 install pandas
    
2. Create a copy of citation file and source paper file and name them to file1.csv and file2.csv respectively

3. Edit file1's header as 'PaperName,Comment' and file2's header as 'paper_title,value'

4. All script file should be in same directory

5. Run the scrips in following order
    script3.py -> script4.py -> cleanScript1.py -> script1.py (finalSent1.txt as output) -> output as (result2.csv) a matrix
