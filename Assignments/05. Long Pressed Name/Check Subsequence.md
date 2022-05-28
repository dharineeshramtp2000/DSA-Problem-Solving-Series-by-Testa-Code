
### You are given an two arrays of integers ```array``` and ```sequence```. You need to check if ```sequence``` is a subsequence of the ```array```. If it is the subsequence, then you need to return ```True```, otherwise return ```False```.

### Constraint:
 - Time - O(n)
 - Space - O(1)

### Sample Input 1:
```
array = [1,2,3,4,5,6,7]
sequence = [1,4,6,7]
````
### Sample Output 1:
```
True
```

### Sample Input 2:
```
array = [9,7,4,6,8,9,0,6,4,-1,2,-10]
sequence = [-10]
````
### Sample Output 2:
```
True
```

### Sample Input 3:
```
array = [2,2,2,2,2,2]
sequence = [2,2,2]
````
### Sample Output 3:
```
True
```

### Sample Input 4:
```
array = [2,2,2]
sequence = [2,2,2,2]
````
### Sample Output 4:
```
False
```

### Sample Input 5:
```
array = [5,6,7,9,3,4,6]
sequence = [5,7,4,6,6]
````
### Sample Output 5:
```
False
```

### Sample Input 6:
```
array = []
sequence = [1]
````
### Sample Output 6:
```
False
```
