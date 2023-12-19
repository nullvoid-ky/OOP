def add_score(subject_score, student, subject, score):
    if student in subject_score:
       subject_score[student][subject] = score
    else :
       new_dict = {}
       new_dict[subject] = score
       subject_score[student] = new_dict
def calc_average_score(subject_score : dict):
  for k , v in subject_score.items():
     subject_score[k] = (sum(v.values()))/len(v)
  return subject_score
