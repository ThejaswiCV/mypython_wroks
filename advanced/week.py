#1 to 8
# 1>> sunday 7>>sat >>holiday
days=[d for d in range(1,8)]
print(days)

week=["holiday"if d==1 or d==7 else "weekday" for d in days ]
# week=["holiday"if d in(1,7) else "weekday" for d in days ]
print(week)