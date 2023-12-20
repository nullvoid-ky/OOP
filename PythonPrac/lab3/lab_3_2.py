def add_score(subject_score, student, subject, score):
  if student in subject_score:
     subject_score[student][subject] = score
  else :
     subject_score[student] = {subject: score}   
  return subject_score
def calc_average_score(subject_score : dict):
  for k , v in subject_score.items():
    subject_score[k] = format((sum(v.values()))/len(v),'.2f')
  return subject_score
