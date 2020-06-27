

This is a toy repository to test a github page. [Click](https://ffliza.github.io/hello-world-tf-Session/.) to see the page.

You can [click](https://github.com/ffliza/hello-world/blob/master/matrix_multiplication_tf.py) to see a basic tensorflow (version 1.0) multiplication using tensorflow.Session. 

<!---  In this example, we have used the modified [minima](https://pages.github.com/themes/) theme. --->

### A Session Object

A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated.

In line [43](https://github.com/ffliza/hello-world/blob/master/matrix_multiplication_tf.py), sess.close() is used. The reason is that a session may own resources, such as tf.Variable, and it is important to release these resources when they are no longer required. To do this, either tf.Session.close method on the session can be invoked, or the session can be used as a context manager like below

```python
with tf.Session() as sess:
  sess.run(...)
```
