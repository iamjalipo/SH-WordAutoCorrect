# WordAutoCorrect
### Auto Correct words based on Shakespeare corpus

The code checks your given word is correct based on Shakespeare's corpus or needs to be replaced.

Instructions:

1- The function 'Deleted_letter' returns all of the possible permutation(whether meaningful or meaningless) of your given word by subtracting one letter.
```python
Deleted_letter('ate')
Output = ['at','te','ae']
```
2- The function 'Replace_letter' returns all of the possible words(whether meaningful or meaningless) that will create by replacing one letter of your given word.
```python
Replace_letter('at')
Output = ['aa','ab',...,'zt']
```
3- The function 'Insert_letter' return all of the possible words(whether meaningful or meaningless) that will create by adding one letter to your given word.
```python
Insert_letter('as')
Output = ['asa','aas' , 'abs' , ... ]
```
4- The function 'edit_one_letter' return all possible permutations of your given word with above three functions as a dictionary.
<br>5- The function 'edit_two_letter' return all possible permutations of your given word using exactly two stacked above functions as a dictionary.
<br>6- If the words in two dictionaries didn't exist in Shakespeare's corpus then we remove them from the dictionaries.
<br>7- Every generated word has unique cost:
  * if the word is created by Deleted_letter & Insert_letter functions then it has cost 1.
  * if the word is created by Replace_letter fucntion, it has cost 2.

8- Now we choose one word with minimum cost as a replacement for the given word.
<br>9- If more than one word has the same minimum cost, we calculate the unigram of them then choose the word with a maximum occurrence probability. 

```python
Example : 
Your word: flw
The code output: flow.
```
