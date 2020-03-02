from django.http import HttpResponse
import random
import tensorflow as tf
def helloworld(request,num1,num2):
    # return HttpResponse("Success")
    tf.compat.v1.disable_eager_execution()
    logs_path='/home/darkshloser/test'
    n1=int(num1)
    n2=int(num2)
    x=tf.compat.v1.placeholder(tf.int32)
    y=tf.compat.v1.placeholder(tf.int32)

    add=tf.add(x,y)
    with tf.compat.v1.Session() as sess:
        summery_writer=tf.compat.v1.summary.FileWriter(logs_path,graph=tf.compat.v1.get_default_graph())

        z=sess.run(add,feed_dict={x:n1,y:n2})
    return HttpResponse("sum of %s and %s is %s "%(num1, num2, z))
