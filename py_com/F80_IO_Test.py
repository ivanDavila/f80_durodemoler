import F80_IO

f80client = F80_IO.F80_MBTCP_Client()
f80client.setHostAddress("192.168.137.22")
f80client.setPort(502)

print(f80client.host_address)
print(f80client.port)

tonelaje = f80client.readDINT(60, 10, False)
print(tonelaje)

f10 = 7.5

f80client.writeDINT(f10, 2, 100, False)