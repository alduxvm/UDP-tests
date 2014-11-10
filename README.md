# UDP-tests

Different ways of communication for the Raspberry Pie and Matlab via UDP. I'm using the timeit module to call a timer in order to get a time between receiving, unpacking and printing (important to notice that I use this way of chronographing with my work with the multiwii board), so, you will see very small numbers... 

## How to make it work?

1. First you need Matlab and Simulink, the .slx file must be opened in simulink, you need to change the ip address where to send the 6 sines signals... 
1. Clone this rep into your rpi, and modify the ip address to yours accordingly
1. Execute which ever example on the rpi and click the run button on simulink and you will start seeing lots of numbers crunching your screen :P

### Socket-Matlab.py

This one is the easiest one, using only the module that provides access to the BSD socket interface.

##### Results on mac:
```
0.00163197517395 0.940350651741 0.0417594239116 0.233919247985 0.128025260911 1.57215267474 0.0832990683
0.000496864318848 0.940350651741 0.0417594239116 0.233919247985 0.128025260911 1.57215267474 0.0832990683
0.00354790687561 0.940290153027 0.0417986474931 0.233891651034 0.128090508358 1.57141204964 0.0836550164245
0.000272989273071 0.940290153027 0.0417986474931 0.233891651034 0.128090508358 1.57141204964 0.0836550164245
```
##### Results on rpi (just time...):
```
0.000607013
0.000509977
0.000748872
0.000519990
```

### Asyncore-Matlab.py

This example makes use of the asycore module. This module provides the basic infrastructure for writing asynchronous socket service clients and servers. 

##### Results on mac:
```
3.50475311279e-05 0.940304279327 0.0418003425002 0.233924299479 0.127610798144 1.57123255258 0.0833177187501
4.50611114502e-05 0.940304279327 0.0418003425002 0.233924299479 0.127610798144 1.57123255258 0.0833177187501
5.3882598877e-05 0.940304279327 0.0418003425002 0.233924299479 0.127610798144 1.57123255258 0.0833177187501
5.79357147217e-05 0.940304279327 0.0418003425002 0.233924299479 0.127610798144 1.57123255258 0.0833177187501
```
##### Results on rpi (just ime...):
```
0.0006768
0.0006248
0.0006201
0.0006239
```

### SocketServer-Matlab.py

This example makes use of the socketserver module. This module simplifies the task of writing network servers. 

##### Results on mac:
```
3.38554382324e-05 0.940361618996 0.0415620431304 0.234024167061 0.124750405008 1.57233430232 0.0928498464041
2.28881835938e-05 0.940361618996 0.0415620431304 0.234024167061 0.124750405008 1.57233430232 0.0928498464041
6.103515625e-05 0.940327703953 0.0415471233428 0.234046339989 0.12441099345 1.57201379089 0.0927638595904
1.81198120117e-05 0.940327703953 0.0415471233428 0.234046339989 0.12441099345 1.57201379089 0.0927638595904
```
##### Results on rpi (just ime...):
```
0.0006768
0.0006248
0.0006201
0.0006239
```

## Conclusions

Seems faster communication using the asyncore module on the mac, on the rpi is fairly similar, is just that the time seems more constant on the asyncore one.