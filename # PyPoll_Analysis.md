# PyPoll Analysis Challenge

## Overview of Project

This project used Python to automate the analysis of Colorado election data. Having completed this project successfully, future audits in colorado will be done automated through Python.

## Election Audit Results

    - Total Votes:
        - 369,711
    - County Votes:
        - Jefferson: 10.5% (38,855)
        - Denver: 82.8% (306,055)
        - Arapahoe: 6.7% (24,801)
    - Largest County Turnout: Denver
    - Votes per Candidate:
        - Charles Casper Stockham: 23.0% (85,213)
        - Diana DeGette: 73.8% (272,892)
        - Raymon Anthony Doane: 3.1% (11,606)
    - Winner of the Election
        - Winner: Diana DeGette
        - Winning Vote Count: 272,892
        - Winning Percentage: 73.8%

## Election Audit Summary

This script of code could be used for any election with some slight alterations. Provided are some examples and explanations.

#### Example 1 (line 48-52 of script)
```
    # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
Here is an example of some easy modifications that could be made, so long as the code downstream is also altered to accomodate it. `candidate_name = row[2]` and `county_name = row[1]` could be altered such that a different variable is extracted from a different column by changing the number in the brackets to fit the column. The name of the variable will likely also change, as well as the variables in the following if conditional statements, but these are easily done.
#### Example 2 (1ine 146-152 of script)
```
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```
Another easy modification that can be done in future audits is to alter what is printed. The variables again would have to be altered to meet the target criteria, but the script could be altered to print whatever information is needed so that it could be readily accessible.

