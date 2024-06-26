import streamlit as st
import pandas as pd
import numpy as np
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("key/fkey.json")

# Create a reference to the Google post.
doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

# # This time, we're creating a NEW post reference for Apple
# doc_ref = db.collection("posts").document("Apple")

# # And then uploading some data to that reference
# doc_ref.set({
# 	"title": "Apple",
# 	"url": "www.apple.com"
# })

# Now let's make a reference to ALL of the posts
posts_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
mylist = list()
for doc in posts_ref.stream():
	st.write("The id is: ", doc.id)
	st.write("The contents are: ", doc.to_dict())
	mylist.append(doc.to_dict())


###
## Try a table
st.table(data=mylist)
print(mylist)
