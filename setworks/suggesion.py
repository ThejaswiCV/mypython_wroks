all_users=["mammoty","surya","tovino","prithvi","dq","asif","vikram","nivin"]

nivin_frnds=["asif","dq","prithvi","vijay","karthi"]
#friends suggesion
dq_frnds=["mammoty","prithvi","asif","vijay","tovino"]
#mutual frnds should show when nivin visit dq profile

all_users_set=set(all_users)
nivin_frnds_set=set(nivin_frnds)
dq_frnds_set=set(dq_frnds)

sugg=all_users_set.difference(nivin_frnds_set)

sugg.discard("nivin")

print(sugg)

mutual=nivin_frnds_set.intersection(dq_frnds_set)
print(mutual)