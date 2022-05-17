#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello")


# In[2]:


a=5
b=10
print(a+b)


# In[4]:


print("Hello World")


# In[1]:


a = 'z'
type(a)


# In[2]:


a = "python"
print(a)


# In[4]:


a = '''
this is a 
multi line string
'''
print(a)


# In[5]:


a = """
this is a
multi line string
"""
print(a)


# In[10]:


a = 10
b = 2
print(a/b)
print(a//b)
print("%0.4f"%(a/b))
# exponent power function
print(a**b)


# In[14]:


a = 10
if a>=10:
    print("positive")
elif a==0:
    print("zero")
else:
    print("negative")


# In[15]:


for i in "python":
    print(i)


# In[19]:


for i in range(1,11,2):
   print(i)


# In[21]:


True or False


# In[22]:


5 and 0


# In[24]:


def sheldon_knock():
    print("knock knock knock jatin")
    print("knock knock knock jatin")
    print("knock knock knock jatin")


# In[26]:


sheldon_knock()
print(10+20)
for i in range(10):
      print(i)
sheldon_knock()


# In[28]:


def sheldon_knock(name,number_of_time=3):
    for i in range(number_of_time):
        print("knock knock knock".format(name))


# In[29]:


sheldon_knock("penny",10)


# In[33]:


def add(a,b):
    print(a+b)
    


# In[34]:


add(10,20)


# In[36]:


def div(a,b):
    try:
        return a/b
    except:
        print('Error')
    finally:
        print('wrapping up')


# In[37]:


div(10,2)


# In[41]:


x = 10
def show():
    global x
    y = "local"
    x+=5
    print(x)
    print(y)


# In[40]:


show()
print(x)


# In[46]:


# here d and e are local variables
# def show (a,b,c,d=10,e=20):
def show(a,b,c,d="something",e="something more"):
     print(a)
     print(b)
     print(c)
     print(d)
     print(e)
show("hello", "world", "python", e ="jatin")


# In[47]:


def show(a,b,c,*args,d=10,e=20,**kwargs):
    print(a)
    print(args)
    print(d)
    print(e)
    print(kwargs)


# In[48]:


show(1,2,3,"jatin", "katyal", d=100, name = "jatin")


# In[49]:


def add(a,b):
    return a+b;


# In[50]:


add = lambda a,b: a+b


# In[51]:


add(1,2)


# In[52]:


a = [("jatin",5),("prateek",10),("ram",1),("arnav",20)]
sorted(a,key=lambda x:x[1])


# In[100]:


users = {
    "jatin": "password",
    "prateek": "coding blocks"
}


# In[85]:


def show(username, password):
    if username in users and users[username] == password:
        print("Hello World")
    else:
        print("Not Authenticated")
    


# In[101]:


show("rohan", "password")


# In[83]:


def add(username, password,a,b):
    if username in users and users[username] == password:
        print(a+b)
    else: 
        print("Not Authenticated")
        


# In[102]:


add("jatin", "password123", 1, 2)


# In[94]:


def login_required(func):
    def wrapper(username, password, *args, **kwargs):
        if username in users and users[username] == password:
            #user is authenticated
            func(*args, **kwargs)
        else:
            print("Not Authenticated")
        return wrapper  


# In[95]:


def temp(*args, **kwargs):
    print(args)
    print(kwargs)
    a = (1,2,3)


# In[93]:


temp(*a)


# In[103]:


def add(a,b):
    print(a+b)


# In[104]:


add(1,2)


# In[105]:


protected_add = login_required(add)


# In[106]:


print(protected_add)


# In[3]:


def fun(a,b,*x,**kwargs):
    print(a)
    print(b)
    print(x)
    print(type(x))
    print(kwargs)
fun(1,2,3,4,10,14, shake= "oreoshake", drink="lemonade", fruit= "Mango")    


# In[ ]:




