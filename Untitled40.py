#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to Add Two Matrices?

# In[9]:


matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

result_matrix = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
for row in result_matrix:
    print(row)


# 2.Write a Python Program to Multiply Two Matrices?

# In[11]:


for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result_matrix:
    print(row)


# 3.Write a Python Program to Transpose a Matrix?

# In[22]:



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result_matrix = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result_matrix[j][i] = matrix[i][j]
for row in result_matrix:
    print(row)


# 4.Write a Python Program to Sort Words in Alphabetic Order?

# In[23]:


words = ["apple", "dog", "elephant"]
sorted_words = sorted(words)
for word in sorted_words:
    print(word)


# 5.Write a Python Program to Remove Punctuation From a String?

# In[24]:


import string
text = "This, is a test string."
text_without_punct = text.translate(str.maketrans("", "", string.punctuation))
print(text_without_punct)


# In[ ]:




