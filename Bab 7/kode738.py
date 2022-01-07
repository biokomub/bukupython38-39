# membuat template
n = "{:{rataan}{lebar}.{presisi}f}"

# melewatkan format sebagai argumen 
print(n.format(123.32, rataan='^', lebar='3', presisi=1))
