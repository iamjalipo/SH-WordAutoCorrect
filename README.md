# WordAutoCorrect
### Auto Correct words based on Shakespeare corpus

The code checks your given word is correct based on Shakespeare's corpus or needs to be replaced.

Instructions:

1- The function 'Deleted_letter' returns all of the possible permutation(whether meaningful or meaningless) of your given word by subtracting one letter.
```
Deleted_letter('ate')
Output = ['at','te','ae']
```
<br>2- The function 'Replace_letter' returns all of the possible words(whether meaningful or meaningless) that will create by replacing one letter of your given word.
```
Replace_letter('at')
Output = ['aa','ab',...,'zt']
```
<br>3- The function 'Insert_letter' return all of the possible words(whether meaningful or meaningless) that will create by adding one letter to your given word.
```
Insert_letter('as')
Output = ['asa','aas' , 'abs' , ... ]
```
