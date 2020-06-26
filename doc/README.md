# A Session Object

A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated. 

In line 35(https://github.com/ffliza/hello-world/blob/master/matrix_multiplication_tf.py), sess.close() is used. The reason is 
a session may own resources, such as tf.Variable, and it is important to release these resources when they are no longer required. 
To do this, either invoke the tf.Session.close method on the session, or use the session as a context manager like below 

```python
with tf.Session() as sess:
  sess.run(...)
```