import json

with open('questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Subject 4 is index 3: "Elaboración de la programación temporalizada de la acción formativa"
# It has 30 questions. Keep first 10, move Q11-Q30 to new subject.
subject4 = data[3]
section4_qs = subject4['questions'][:10]   # Q1-Q10
test_final_qs = subject4['questions'][10:] # Q11-Q30

# Clean up option d of Q10 in section4 - remove the extra "TEST FINAL" text that was appended
for q in section4_qs:
    for i, opt in enumerate(q['options']):
        if 'Programación didáctica de acciones formativas para el empleo. - TEST FINAL' in opt:
            # Clean the option and correctAnswer
            clean_opt = opt.replace(' Programación didáctica de acciones formativas para el empleo. - TEST FINAL', '')
            q['options'][i] = clean_opt
            if q.get('correctAnswer') and 'Programación didáctica de acciones formativas para el empleo. - TEST FINAL' in q['correctAnswer']:
                q['correctAnswer'] = clean_opt

# Update subject 4 with only 10 questions
data[3]['questions'] = section4_qs

# Create new subject for TEST FINAL
new_subject = {
    "subject": "Test Final - Programación didáctica acciones formativas",
    "unit": "Semestral",
    "questions": test_final_qs
}

data.append(new_subject)

with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done! Subject 4 now has {len(section4_qs)} questions")
print(f"New subject 'Test Final' has {len(test_final_qs)} questions")
print(f"Total subjects: {len(data)}")
