score = {
    "윤아" : {"국어":85, "수학":92, "영어":69},
    "정국" : {"국어":55, "수학":72, "영어":58},
    "태연" : {"국어":45, "수학":52, "영어":48},
    "보검" : {"국어":85, "수학":72, "영어":98}
}

# 학생별로 평균
avg = {}
for name in score.keys():
    total = sum(score[name].values())
    sub_count = len(score[name])
    avg[name] = round(total/sub_count,2)
# print(avg)


# 평균이 70점 이상인 학생
avg_over={}
for name in avg.keys():
    if avg[name] >= 70:
        avg_over[name] = avg[name]
# print(avg_over)

# 평균정렬 (내림차순)
avg_sort_name=[]
avg_sort_score=[]
for i in avg.keys():
    avg_sort_score.append(avg[i])
    avg_sort_score.sort(reverse=True)
    avg_sort_name.append(i)
    avg_sort_score.sort(reverse=True)

print(avg_sort_name)
print(avg_sort_score)

avg_sort_dict={}
for name, score in zip(avg_sort_name,avg_sort_score):
    avg_sort_dict[name] = score

print(avg_sort_dict)




# 과목별 최고점수
# max_score={}
# for name in score.keys():
#     for sub in score[name].keys():
#         if sub in score[name]:
#             print(sub,score[name][sub])


