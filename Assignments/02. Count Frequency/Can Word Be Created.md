### You are given two strings ```language``` and ```word```. You need to return ```True``` if you can create ```word``` from the given ```language``` else return ```False```. For the word to be created from the given language, the frequency of every distinct character from ```word``` should be less than or equal to the frequency of the corresponding character in ```language```

### Constraint:
 - Time - O(n + m) where n and m are the lengths of the input strings.
 - Space - O(1)

### Sample Input 1:
```
language = "vdsdefghjkoiuytredfvbn"
word = "vkoif"

````
### Sample Output 1:
```
True
```

### Sample Input 2:
```
language = "thehyebsvshjllans"
word = "zxhudhhd"

````
### Sample Output 2:
```
False
```

### Sample Input 3:
```
language = "thefj"
word = "isthispossible"

````
### Sample Output 3:
```
False
```

### Sample Input 4:
```
language = "aaaaabbbaujajjka"
word = "a"

````
### Sample Output 4:
```
True
```

### Sample Input 5:
```
language = "wsdcvbjkollkjhytrdsx"
word = "wsdcvbjkollkjhytrdsx"

````
### Sample Output 5:
```
True
```
