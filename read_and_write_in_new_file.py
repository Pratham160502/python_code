f1=open("rossum.jpg","rb") 
f2=open("newpic.jpg","wb") 
bytes=f1.read() 
f2.write(bytes) 
print("New Image is available with the name: newpic.jpg")
