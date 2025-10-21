score = {
    '윤아': {'국어':99, '수학':99, '영어':99},
    '정국': {'국어':15, '수학':12, '영어':13},
    '태연': {'국어':41, '수학':25, '영어':78},
    '보검': {'국어':75, '수학':83, '영어':75}
}

# 학생별 평균을 구하고 평균이 70점이상인 학생
# 평균 정렬: 내림차순
# ex) {'보검': 77.67, '윤아': 77.0}
result = {}
avg_student={}
for name in score.keys():
    total = sum(score[name].values())
    sub_count = len(score[name])
    avg = round(total / sub_count, 2)
    avg_student[name] = avg

    # 80점 이상 출력
    avg_80 = list(filter(lambda x: x[1] >= 80, result.items()))


    if avg >= 70:
        result[name] = avg


sorted_name = sorted(result, key=result.get, reverse=True)
sorted_result = {}
for name in sorted_name:
    sorted_result[name] = result[name]

# print(sorted_result)


# 각 과목에서 최고점 학생
# ex) {'국어': '보검', '수학': '윤아', '영어': '태연'}
subjects = ['국어', '수학', '영어']
top = {}
for subject in subjects:
    top_score = 0
    top_name = ''
    for name in score:
        if score[name][subject] > top_score:
            top_score = score[name][subject]
            top_name = name
    top[subject] = top_name

# print(top)


