#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
#read image
img = cv2.imread('baby.jpg',0)
#print(img)
#show image
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    #write image
    cv2.imwrite('baby_copy1.jpg',img)
    cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




