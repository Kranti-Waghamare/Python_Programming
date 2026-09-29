import tensorflow as tf

tensor1 = tf.constant([10, 20, 30])
tensor2 = tf.constant([1, 2, 3])

addition = tf.add(tensor1, tensor2)
print("Addition is : ",addition)

substraction = tf.subtract(tensor1, tensor2)
print("Substraction is : ",substraction)

multiplication = tf.multiply(tensor1, tensor2)
print("Multiplication is : ",multiplication)

division = tf.divide(tensor1, tensor2)
print("division is : ",division)

square = tf.square(tensor1)
print("square : ",square)

sum = tf.reduce_sum(tensor1)
print("Reduced sum : ",sum)

mean = tf.reduce_mean(tensor1)
print("Mean is : ",mean)