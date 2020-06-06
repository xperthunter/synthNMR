import synthnmr as sn

print('hello synth')

xyz, pi = sn.random_spectrum(points=10)

print(xyz.shape)
print(pi.shape)

print(pi[:,2:4])