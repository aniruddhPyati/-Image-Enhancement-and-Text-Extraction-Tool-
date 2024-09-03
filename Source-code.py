#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[16]:


import cv2


# In[17]:


img= cv2.imread("text-image.jpeg")


# In[18]:


img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[19]:


img=cv2.resize(img, (560,900))


# In[20]:


cv2.imshow("title",img)
cv2.waitKey(0)


# In[21]:


#thresholding


# In[22]:


_, result = cv2.threshold(img,20, 220,cv2.THRESH_BINARY)


# In[23]:


adaptive_result = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,35,10)


# In[29]:


cv2.imshow("title",img)
cv2.imshow("adpative",adaptive_result)
cv2.waitKey(0)


# In[11]:


import pytesseract


# In[12]:


pip install pytesseract


# In[13]:


import pytesseract


# In[14]:


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[15]:


text = pytesseract.image_to_string(adaptive_result)
print(text)


# In[ ]:




