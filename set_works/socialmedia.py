ig_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}

mohanlal_following={"prithvi","vijay","lalu"}
dq_friends={"prithvi","fahad","sureshgopi","lalu"}

mohanlal_suggestion=ig_users.difference(mohanlal_following)
mohanlal_suggestion.discard("mohanlal")
print(mohanlal_suggestion)


mutual_friends=mohanlal_following.intersection(dq_friends)
print(mutual_friends)