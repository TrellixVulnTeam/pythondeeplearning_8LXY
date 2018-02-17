from random import randint
import numpy as np
har = np.random.randint(0,20, size=(15))
print("Array: %s"   %har)
print("Most Frequent integers in the array:")
print(np.bincount(har).argmax())