# Results of OpenBCI Translation Application Research

## Research Information
Research was conducted within 2 days: 19 December 2024 and 20 December 2024.

Research was conducted on 20 people.

One person participated in the research twice. During first day of research participant had sufferred to the migraine which might have impacted research. However during second day of research the same participant was not sufferring to migraine anymore and was willing to participate again in the studies. Hence file ```1734615086__migraine.csv``` and file ```1734699358__no_migraine.csv``` both correspond to the same person but with and without health condition that may impact results.

## Data Files

There are two main folders containing data files:
- ```recordings``` - containing original data recordings from the studies,
- ```manually_labeled``` - containing manually labeled (after the reasearch was finished) data.

Manually labeled data **may not be** perfectly accurate when it comes to the time of labeling.

Additionally due to human error of research team, some of the files **do not contain** so called *relax period* in the beginning.

## Data Format

Each file consists of a header and data entries (rows).

Each row after the header is a single entry recorded from the EEG OpenBCI helm with default interval of 250Hz.

Columns in the files:
- ```Channel 1``` - data recorded from first electrode
- ```Channel 2``` - data recorded from second electrode
- ```Channel 3``` - data recorded from third electrode
- ```Channel 4``` - data recorded from fourth electrode
- ```Channel 5``` - data recorded from fifth electrode
- ```Channel 6``` - data recorded from sixth electrode
- ```Channel 7``` - data recorded from seventh electrode
- ```Channel 8``` - data recorded from eight electrode
- ```Weighted Output``` - result of simple weighted average computation

```manually_labeled``` files contain one more additional column:
- ```State``` - Label informing about current state of participant. ```R``` stands for *Relaxed* and ```F``` stands for *Focused*
