import json
import pandas as pd

src = "./Current Flashcard/final_output.json"
dest = "./Current Flashcard/output.xlsx"


with open(src, "r", encoding="UTF-8") as json_:
    json_content = json.load(json_) #list type output
    
df = pd.DataFrame(json_content)
df.to_excel(dest, index=False, engine="openpyxl")