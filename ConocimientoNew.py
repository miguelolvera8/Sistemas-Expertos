# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:20:33 2024

@author: Usuario
"""

# Base de datos simulada para almacenar conocimiento
knowledge_base = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "Como estas?": "Estoy bien, gracias. ¿Y tú?",
    "de que te gustaría hablar?": "Puedo hablar de muchos temas. ¿Tienes alguna preferencia?",
}

# Pregunta predeterminada para adquirir nuevo conocimiento
default_question = "No entiendo. ¿Puedes proporcionarme más información sobre eso?"

def mostrar_menu():
    print("Respuestas posibles:")
    for key in knowledge_base.keys():
        print(f"- {key}")

def chatbot():
    print("Bienvenido al Chatbot. Ingresa 'exit' para salir.")
    
    while True:
        mostrar_menu()
        user_input = input("Tú: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Hasta luego. ¡Espero verte pronto!")
            break
        
        response = knowledge_base.get(user_input, default_question)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
