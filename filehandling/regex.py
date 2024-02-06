import re

st = "https://www.google.com/search?h/petsexpert/siamese-cat-price-in-india/blog/macaws-prices-purchase-cost-supplies-food-and-more/mynextpet.in/macaw-parrot-price-in-india/parthiv/"
res = re.findall(r"(.*?)/", st)
for i in range(len(res)):
    print("Before: ", ("" if i == 0 else res[i-1]))
    print("Between: ", res[i])
    print("After: ", ("" if i == len(res)-1 else res[i+1]))
