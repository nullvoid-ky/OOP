def add_score(subject_score, subject, score):
  subject_score[subject] = score
  return subject_score
def calc_average_score(subject_score : dict):
  avr = (sum(subject_score.values()))/len(subject_score)
  return format(avr, '.2f')
