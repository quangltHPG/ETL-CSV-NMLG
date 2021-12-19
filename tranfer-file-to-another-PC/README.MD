OPEN CMD
CHECK PORT
	netstat -a -n
CHECK PID PORT
	netstat -a -n -o | find "(#port number)"
	netstat -ano | findstr:(#port number)
EX:
	netstat -a -n -o | find "123456"
	netstat -ano | findstr:5001
	TCP    0.0.0.0:5001           0.0.0.0:0              LISTENING       21028
KILL PORT = KILL PID
	taskkill/pid (#number PID) /F
EX
	taskkill/pid 21028 /F
	SUCCESS: The process with PID 21028 has been terminated.