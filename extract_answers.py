import re
import json

# Leer el contenido extraido de los PDFs
with open('extracted_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Patrones para encontrar respuestas
answer_patterns = [
    # Para preguntas con respuesta directa (ej: "A. Texto")
    (r'([A-D])\.\s*([^A-D\n]+?)(?=\n*[A-D]\.|$)', 'direct'),
    # Para respuestas con "Solución:" o similar
    (r'solución:\s*\n*([A-D][^\n]+)', 'solution'),
    # Para respuestas al final de página
    (r'respuesta:\s*\n*([A-D][^\n]+)', 'answer'),
]

subjects = {
    'Test Final.pdf': 'Test Final',
    'Test Modulo 1.pdf': 'Test Modulo 1',
    'Test Modulo 2.pdf': 'Test Modulo 2',
    'Test Modulo 3.pdf': 'Test Modulo 3',
    'Test Modulo 4.pdf': 'Test Modulo 4'
}

def extract_questions_answers(text):
    # Dividir por PDF
    pdf_sections = text.split('='*60)
    answers = {}
    
    for section in pdf_sections:
        if '===' in section:
            # Identificar PDF
            for pdf_name, subject in subjects.items():
                if pdf_name in section:
                    current_subject = subject
                    break
            
            # Extraer preguntas y respuestas
            lines = section.split('\n')
            current_question = None
            question_text = ""
            question_number = 1
            
            for line in lines:
                line = line.strip()
                if line and ('.' in line[:10] and not line.startswith('---')):
                    # Nueva pregunta detectada
                    if current_question:
                        # Guardar pregunta anterior
                        if current_question not in answers:
                            answers[current_question] = []
                        answers[current_question].append({
                            'question': question_text.strip(),
                            'answer': None  # Se llenará después
                        })
                    
                    # Nueva pregunta
                    current_question = f"{current_subject}_{question_number}"
                    question_text = line
                    question_number += 1
                elif current_question and line:
                    question_text += " " + line
            
            # Última pregunta
            if current_question:
                if current_question not in answers:
                    answers[current_question] = []
                answers[current_question].append({
                    'question': question_text.strip(),
                    'answer': None
                })
    
    return answers

# Extraer preguntas y respuestas
answers = extract_questions_answers(text)

print("Respuestas extraídas:")
for question_id, question_data in answers.items():
    for i, q in enumerate(question_data):
        print(f"{question_id}_{i}: {q['question'][:100]}...")
        print(f"Respuesta: {q['answer']}")
        print("-" * 50)