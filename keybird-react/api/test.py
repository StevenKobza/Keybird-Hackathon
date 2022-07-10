import os
import tensorflow as tf

#tf.test.gpu_device_name()


#print(os.getcwd())
#if ("gen_file" in os.listdir(os.getcwd() + "/api/")):
    #print("hi")
#path = "../../Keybird-Hackathon/Deep Learning/gen_file"
path = os.getcwd() + "/gen_file/"
os.chdir(path)
print(os.listdir(os.getcwd()))

#exec(open("gen_json.py").read())