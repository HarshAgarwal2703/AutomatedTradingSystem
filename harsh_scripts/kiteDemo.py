import socket
# client code to connect with API bridge
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 56789    # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    #ID,Type,Symbol,OrderType,TrigPrice,Price,Qty,InstrumentName,StrategyTag"
    # Symbol = Symbol | Expiry | Strike | OptionType
    # TrigPrice = TrigPrice | StopLoss | SquareOff | TrailingTicks
    # StrategyTag = StrategyTag | Port
    print(s)
    #s.sendall(b"8,LE,SBIN,M,1,180,1,EQ,STG11")
    #s.sendall(b"8,SE,RELIANCE,L,1,180,1,EQ,STG11")
   # s.sendall(b"8,SE,HDFC,L,1,1200,100,EQ,STG11")
    #s.sendall(b"8,SE,INFY|30MAY2019|130|PE,L,1,2000,50,OPTSTK,STG11")
    s.sendall(b"8,LE,MARUTI,L,1,180,1,EQ,STG11")

    data = s.recv(1024)

print('Received', repr(data))