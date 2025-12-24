import chardet

# 1. Detect encoding
with open("data/products.csv", "rb") as f:
    raw = f.read()
result = chardet.detect(raw)
print(result)