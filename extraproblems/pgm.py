
data = {
    "Krishna":[67,68,69],
    "Arjun": [70,98,63],
    "Malika":[52,56,60]
}

def get_query_value(query):
  
    query_value = data.get(query)

    if query_value is not None:
        return query_value
    else:
        return "Name not found in the dictionary."

query_string = "Malika"

result = get_query_value(query_string)
print(result)
print(sum(result)/3)
