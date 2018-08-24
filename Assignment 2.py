
# coding: utf-8

# In[12]:


values= input("Enter comma separated values")
l=values.split(",")
print (l)


# In[14]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[16]:


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[21]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens\n")

