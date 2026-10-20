# --- 1. BASIC SCORING PRESETS ---


def calculate_standard(correct_count, weight_correct):
  """Standard Mode: Only calculates correct answers without any penalties."""
  return correct_count * weight_correct

def calculate_penalty(correct_count, wrong_count, weight_correct, weight_wrong):
  """Penalty Mode: Correct answers add points, wrong answers subtract points.

  weight_wrong is typically negative (e.g., -1).
  """
  score = (correct_count * weight_correct) + (wrong_count * weight_wrong)
  return max(0, score)  # Prevents final score from dropping below zero

def calculate_strict(correct_count, wrong_count, weight_correct, weight_wrong):
  """Strict Mode: Wrong answer penalties are doubled for harsher grading."""
  penalty = weight_wrong * 2 if weight_wrong < 0 else -2
  score = (correct_count * weight_correct) + (wrong_count * penalty)
  return max(0, score)

def calculate_percentage(earned_score, max_possible_score):
  """Percentage Scale: Converts total earned score into a 0-100 scale."""
  if max_possible_score == 0:
    return 0.0
  percentage = (earned_score / max_possible_score) * 100
  return round(percentage, 2)

def calculate_pass_fail(score, threshold_kkm, bonus_points):
  """Pass-Fail Bonus Mode: Grants extra bonus points if the score meets

  or exceeds the passing threshold (KKM).
  """
  if score >= threshold_kkm:
    return score + bonus_points
  return score

# --- 2. ADVANCED SCORING PRESETS ---

def calculate_difficulty(user_answers, question_weights):
  """Dynamic Difficulty Scaling: Assigns unique weights to each question

  based on its individual difficulty level.
  """
  total_score = 0
  for is_correct, weight in zip(user_answers, question_weights):
    if is_correct:
      total_score += weight
  return total_score

def calculate_streak(user_answers, base_weight):
  """Streak Multiplier Combo: Rewards consecutive correct answers

  with escalating point multipliers.
  """
  total_score = 0
  current_streak = 0
  for is_correct in user_answers:
    if is_correct:
      current_streak += 1
      multiplier = (
          1 + (current_streak - 1) * 0.1
      )  # +10% bonus for every streak count
      total_score += base_weight * multiplier
    else:
      current_streak = 0  # Reset streak on wrong answer
  return round(total_score, 2)

def calculate_confidence(answers_data, base_weight):
  """Confidence-Based Scoring: Factors in the user's confidence level

  (e.g., guessing vs. absolute certainty).
  """
  total_score = 0
  for item in answers_data:
    is_correct = item["correct"]
    conf = item["confidence"]  # e.g., 1 = Low, 2 = Medium, 3 = High
    if is_correct:
      total_score += base_weight * conf
    else:
      total_score -= base_weight * 0.5 * conf  # Scaled penalty for overconfidence
  return max(0, total_score)

def calculate_diminishing(user_answers, base_weight):
  """Diminishing Returns / Fatigue Mode: Questions placed later in the quiz

  carry higher multipliers to reward endurance.
  """
  total_score = 0
  total_questions = len(user_answers)
  for index, is_correct in enumerate(user_answers):
    if is_correct:
      position_multiplier = 1 + (index / total_questions)
      total_score += base_weight * position_multiplier
  return round(total_score, 2)

def calculate_gamble(base_score, risk_multiplier):
  """Asymmetric Gamble / High-Stakes Mode: Multiplies the final base score

  by a high-risk factor chosen by the user at the start.
  """
  return base_score * risk_multiplier