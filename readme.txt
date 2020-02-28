In addition to your programs, you must also submit a README file with clearly
dilenated sections for the following.

0. Please write down the full names and netids of both your team members.
Ruslan Volyar (rv379) and Abishek Koutha(Ak1421)

1. Briefly discuss how you implemented your recursive client functionality.
Because we only have two dns servers in this project, we used a simple if statement to route our queries.  First we query the the RS server.  
If it returns an A record, we have found a match and return it. If it returns an NS record, we connect to the TS server and query it for the IP.

2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
   No known issues. Everything works as expected.
   
3. What problems did you face developing code for this project?
One issue we had was a strange file descriptor error that was being thrown as soon as any client connected to our server.  
We believe it happened because we kept opening an already open socket.  We fixed it by moving the connection logic outside of the while loop.

4. What did you learn by working on this project?
Ruslan - This project further reinforced my knowledge on how DNS servers work.  I have setup websites in the past, but when it came time to configuring the DNS I always followed online tutorials. 
Now I can say that I understand how DNS works on the backend and can figure out any website problems using what I learned from this class.
