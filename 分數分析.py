scores=[78,92,65,88,73,95,81,69,84,90]

highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)
top_three_scores = sorted(scores, reverse=True)[:3]

print("===成績分析===")
print("資料筆數:" ,len(scores))
print("最高分:" ,highest_score)
print("最低分:" ,lowest_score)
print("平均:", average_score)  
print("前三名:", top_three_scores)