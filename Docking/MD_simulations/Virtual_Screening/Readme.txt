# Virtual Screening-Analysis

## Python Scripts for Virtual Screening Results Analysis

### Introduction

<i>vs_analysis.py</i> script provides top poses amongst the screened compounds with the lowest binding affinity.
It parses all log files present in a directory and then fetches the desired (user input) number of compounds with the binding affinity of the top pose given in the log file. 
This script also allows users to get binding affinities of compounds based on a user inputted cutoff value. The user can provide a threshold for binding affinities above which all affinities present in the files will be provided in an output file.
The output file consists of filename and corresponding binding affinity sorted in ascending order.
You can run it on Linux as well as on Windows using the command given below. Don't forget to provide the full path to this file, if it is saved in another directory.

<i>vs_analysis_compoun.py</i> script allows users to search for specific binding affinities corresponding to compound names. Users have to provide a compound name as an argument given that the same compound name is present in the log filenames.

### Usage:

To use <i>vs_analysis.py</i> script, run the following command:

```$ python vs_analysis.py``` 

OR

```$ python3 vs_analysis.py```


Since it is an interactive script, it will prompt user during its execution.


To use <i>vs_analysis_compound.py</i> script, run the following command:

```$ python vs_analysis_compound.py <compound-name>``` 

OR

```$ python3 vs_analysis_compound.py <compound-name>```

***For example,***
You have 50 log files in your directory and you want to fetch the top 20 results/poses sorted with the lowest binding affinities.
Then run the above command and while prompted enter 20. It will provide the top 20 results in the 'output.txt' file.
Remember to enter a valid number, i.e., the number you enter must be less than or equal to the number of files present in the directory.

***NOTE:
This script screens for the log files containing the word 'log' in their filenames.
It is recommended to name your log files along with the name of a compound. That would make the results more presentable and easy to understand.***


For more information on this script, please visit the following links:
https://bioinformaticsreview.com/20210509/vs-analysis-a-python-script-to-analyze-virtual-screening-results-of-autodock-vina/
https://bioinformaticsreview.com/20220329/how-to-sort-binding-affinities-based-on-a-cutoff-using-vs_analysis-py-script/


