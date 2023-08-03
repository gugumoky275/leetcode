#### First solution:
Iterate string and at each point consider the current longest substring possible, compare it to global max.
Keep a map of each character in string to what position in string and if a dupliccate character is found, delete
all characters in substring that are up untill the duplicate one.

O(N) memory O(N^2) time beacuse of the iteration on substring when deleting

#### Second solution (improvement), beats 99.24%:
Iterate string and keep last index for each character ever found in string, at each step consider the longest
substring to be formed with characters prior. When a duplicate character is found check if it is part of current
substring (it's last position is in the right of starting position of the substr) and if so update starting position.
Basically the same as first solution but without the need of keeping evidence of all chas in substr and so the
necessity of deletion.

A note is the usage of implicit value in dict.get function, which is to be claimed fast due to ease of implementation
in bytecode.

#### CPP solution from 2 years ago beats 100%:
Similar to prev python solution, but rather more complicated to understand :D
It beats 100% solutions tho

A note here is that the longer the array at some point the main if will only go to else branch which can be very well
simplified by branching predictor in CPUs, and other than this one there are no branches only max and mins, facilitating
instruction pipeline (and instruction caching).
